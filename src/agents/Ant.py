from random import choice
from pade.core.agent import Agent
from pade.misc.utility import display_message
from ..grid.grid import Grids
from pade.behaviours.protocols import TimedBehaviour


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.choose_path()
        display_message(self.agent.aid.localname, self.agent.current_pos)

class Ant(Agent):
    position = 499

    def __init__(self, aid, current_pos = [0,0]):
        super(Ant, self).__init__(aid=aid)
        self.carrying = False
        self.current_pos = current_pos
        self.last_pos = current_pos

        comp_temp = ComportTemporal(self, .1)

        self.behaviours.append(comp_temp)

    def choose_path(self):
        to_food_path = []
        to_home_path = []
        find_food = None
        find_home = None

        if self.carrying:
            for pos_x in range(3):
                for pos_y in range(3):
                    if [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y] == Grids().initial_position:
                        find_home = [(self.current_pos[0] - 1) + pos_x, (self.current_pos[1] -1) + pos_y]
                        display_message(self.aid.localname, "Achei o formigueiro")
                        break

                    if (self.check_grid_limits(pos_x, pos_y)):
                        continue

                    to_home_path.append({ 
                        "coordinates": [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y], 
                        "value": Grids().grid_to_home.item((self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y)
                    })

            temp_to_food = Grids().grid_to_food
            temp_to_food[self.current_pos[0], self.current_pos[1]] += 1
            Grids().grid_to_food = temp_to_food

            self.last_pos = self.current_pos


            if find_home:
                self.carrying = False
                self.current_pos = find_home
 
            else:
                to_home_path.sort(key=lambda lst: lst['value'], reverse=True)
                self.current_pos = to_home_path[0]["coordinates"]

        # Procurando comida
        else:
            for pos_x in range(3):
                for pos_y in range(3):
                    if [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y] == Grids().food_position:
                        find_food = [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y]
                        display_message(self.aid.localname, "Achei comida nos arredores")
                        break

                    if (self.check_grid_limits(pos_x, pos_y)):
                        continue

                    elif food_path := Grids().grid_to_food.item((self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y):                        
                        to_food_path.append({ 
                            "coordinates": [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y], 
                            "value": food_path
                        })

                    to_home_path.append({ 
                        "coordinates": [(self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y], 
                        "value": Grids().grid_to_home.item((self.current_pos[0] -1) + pos_x, (self.current_pos[1] -1) + pos_y)
                    })


            #display_message(self.aid.localname, f"Home path possui {len(to_food_path)} elementos : {(to_food_path)} last position: {self.last_pos}")

            temp_to_home = Grids().grid_to_home
            temp_to_home[self.last_pos[0], self.last_pos[1]] += 1
            Grids().grid_to_home = temp_to_home

            self.last_pos = self.current_pos

            if find_food:
                self.carrying = True
                self.current_pos = find_food

            elif len(to_food_path) > 0:
                to_food_path.sort(key=lambda lst: lst['value'], reverse=True)
                self.current_pos = to_food_path[0]["coordinates"]

            else:
                to_home_path.sort(key=lambda lst: lst['value'])
                no_pheromones = list(filter(lambda lst: lst['value'] == 0, to_home_path))

                if len(no_pheromones) > 0:
                    self.current_pos = choice(no_pheromones)["coordinates"]

                else:
                    self.current_pos = to_home_path[0]["coordinates"]


    def check_grid_limits(self, pos_x, pos_y):
        if (self.current_pos[0] -1) + pos_x == self.last_pos[0] and \
            (self.current_pos[1] -1) + pos_y == self.last_pos[1]:
            return True
        elif (self.current_pos[0] -1) + pos_x == self.current_pos[0] and \
            (self.current_pos[1] -1) + pos_y == self.current_pos[1]:
            return True
        elif ((self.current_pos[0] -1) + pos_x) < 0:
            return True
        elif ((self.current_pos[1] -1) + pos_y) < 0:
            return True
        elif ((self.current_pos[0] -1) + pos_x) > Grids().limit:
            return True
        elif ((self.current_pos[1] -1) + pos_y) > Grids().limit:
            return True
        return False
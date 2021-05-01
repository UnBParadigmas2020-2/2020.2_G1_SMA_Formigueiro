from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from random import choice
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from sys import argv
import numpy as np



class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        a = self.agent.position
        a = [a-11, a-10, a-9, a-1, a+1, a+11, a+10, a+9]
        possible_paths = []

        for position in a:
            if position >= 0 and position <= 1000:
                possible_paths.append(position)

        self.agent.position = self.agent.choose_path(possible_paths)
        display_message(self.agent.aid.localname, self.agent.grid[self.agent.position])
        

class Ant(Agent):
    position = 499

    def __init__(self, aid, grid, food_position):
        super(Ant, self).__init__(aid=aid)
        self.grid = grid
        self.food_position = food_position
        self.carrying = False
        comp_temp = ComportTemporal(self, .1)

        self.behaviours.append(comp_temp)

    def choose_path(self, possible_paths:list):
        preferred_path = []
        secondary_path = []

        for position in possible_paths:
            if self.grid[position][1] < 1:              #prefere andar por caminhos sem feromonio "home"
                preferred_path.append(position)
            else:
                secondary_path.append(position)

        if not self.carrying:
            self.grid[self.position] += [0,1,0]
            if len(preferred_path) > 0:
                if self.food_position in preferred_path:
                    self.carrying = True
                    return self.food_position
                else:
                    return choice(preferred_path)
            else:
                return choice(secondary_path)
        else:
            return self.food_position


if __name__ == '__main__':

    grid = np.column_stack((np.arange(1000).reshape(1000,1),np.zeros((1000,2),dtype=int)))
    agents_per_process = 10
    food_position = 769
    c = 0
    agents = list()
    for i in range(agents_per_process):
        port = int(argv[1]) + c
        agent_name = f'Ant_{i}'

        ant = Ant(AID(name=agent_name), grid, food_position)

        agents.append(ant)
        c += 1000

    start_loop(agents)


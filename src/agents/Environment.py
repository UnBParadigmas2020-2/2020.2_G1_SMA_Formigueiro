from random import choice
from pade.core.agent import Agent
from ..grid.grid import Grids
from pade.behaviours.protocols import TimedBehaviour


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.decrease_pheromone()


class EnvironmentAgent(Agent):
    def __init__(self, aid, dimension=(30, 30)):
        super(EnvironmentAgent, self).__init__(aid=aid)
        x = range(0, dimension[0])
        y = range(0, dimension[1])
        self.food_position = [choice(x), choice(y)]
        self.anthill_position = [choice(x), choice(y)]
        self.behaviours.append(ComportTemporal(self, 1.))

    def decrease_pheromone(self):
        temp_to_food = Grids().grid_to_food
        for i in range(len(temp_to_food)):
            for j in range(len(temp_to_food[0])):
                if temp_to_food[i][j] >= 1:
                    temp_to_food[i][j] -= 1

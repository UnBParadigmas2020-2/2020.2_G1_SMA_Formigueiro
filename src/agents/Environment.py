from random import choice
from pade.core.agent import Agent
from ..grid.grid import Grids
from ..settings import  AGENT_TIME
from pade.behaviours.protocols import TimedBehaviour


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.decrease_pheromone()


class EnvironmentAgent(Agent):
    def __init__(self, aid):
        super(EnvironmentAgent, self).__init__(aid=aid)
        self.count = 0
        self.evaporate_time = int(Grids().limit * 3.5)

        self.behaviours.append(ComportTemporal(self, AGENT_TIME))

    def decrease_pheromone(self):
        if self.count == self.evaporate_time:
            for index_x, x in enumerate(Grids().grid_to_home):
                for index_y, y in enumerate(x):
                    if Grids().grid_to_home[index_x, index_y] > 0:
                        Grids().grid_to_home[index_x, index_y] -= 1
                    if Grids().grid_to_food[index_x, index_y] > 0:
                        Grids().grid_to_food[index_x, index_y] -= 1
            self.count = 0
        
        self.count += 1

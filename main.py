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
        for index in a:
            if self.agent.grid[index][1] < 1:
                possible_paths.append(index)
        print('Possiveis caminhos: ' + str(possible_paths))
        if len(possible_paths) > 0:
            self.agent.grid[self.agent.position] += [0,1,0]
            self.agent.position = choice(possible_paths)
            display_message(self.agent.aid.localname, self.agent.grid[self.agent.position])


class Ant(Agent):
    grid = np.column_stack((np.arange(1000).reshape(1000,1),np.zeros((1000,2),dtype=int)))
    position = 499

    def __init__(self, aid):
        super(Ant, self).__init__(aid=aid)
        comp_temp = ComportTemporal(self, .1)

        self.behaviours.append(comp_temp)



if __name__ == '__main__':

    agents_per_process = 1
    c = 0
    agents = list()
    for i in range(agents_per_process):
        port = int(argv[1]) + c
        agent_name = f'Ant_{i}'

        ant = Ant(AID(name=agent_name))

        agents.append(ant)
        c += 1000

    start_loop(agents)
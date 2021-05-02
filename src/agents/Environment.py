from random import choice
from pade.core.agent import Agent
from ..grid.grid import Grids
from pade.behaviours.protocols import TimedBehaviour


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()

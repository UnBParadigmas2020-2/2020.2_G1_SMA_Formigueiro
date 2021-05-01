from singleton_decorator import singleton
import numpy as np


@singleton
class Grids():
    def __init__(self, shape = (1000, 1000)):
        self._grid_to_home = np.zeros(shape=shape)
        self._grid_to_food = np.zeros(shape=shape)

    @property
    def grid_to_home(self):
        return self._grid_to_home
    
    @property
    def grid_to_food(self):
        return self._grid_to_food
from singleton_decorator import singleton
import numpy as np


@singleton
class Grids():
    def __init__(self, shape = (30, 30)):
        self._grid_to_home = np.zeros(shape=shape)
        self._grid_to_food = np.zeros(shape=shape)
        self.limit = shape[0]
        self.food_position = [10,10]
        self.initial_position = [0, 0]

    @property
    def grid_to_home(self):
        return self._grid_to_home

    @grid_to_home.setter
    def grid_to_home(self, value):
        self._grid_to_home = value
    
    @property
    def grid_to_food(self):
        return self._grid_to_food
    
    @grid_to_food.setter
    def grid_to_food(self, value):
        self._grid_to_food = value
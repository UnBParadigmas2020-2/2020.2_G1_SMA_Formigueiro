from singleton_decorator import singleton
from ..settings import CANVAS_SIZE
import numpy as np
from random import choice
from threading import Lock


@singleton
class Grids():
    def __init__(self, shape = (CANVAS_SIZE, CANVAS_SIZE)):
        self._grid_to_home = np.zeros(shape=shape)
        self._grid_to_food = np.zeros(shape=shape)
        self.limit = shape[0]
        self._lock = Lock()
        self.food_positions = [
            #[10,10],
            [choice(list(range(CANVAS_SIZE - 1))), choice(list(range(CANVAS_SIZE - 1)))],
            [choice(list(range(CANVAS_SIZE - 1))), choice(list(range(CANVAS_SIZE - 1)))],
            [choice(list(range(CANVAS_SIZE - 1))), choice(list(range(CANVAS_SIZE - 1)))],
        ]
        # self.initial_position = [1,1]
        self.initial_position = [choice(list(range(CANVAS_SIZE - 1))), choice(list(range(CANVAS_SIZE - 1)))]
        self._around_food = []
        self._around_base = []
        for pos_x in range(3):
            for pos_y in range(3):
                self._grid_to_home[self.initial_position[0] - 1 + pos_x, self.initial_position[1] - 1 + pos_y] = 100
                self._around_base.append([self.initial_position[0] - 1 + pos_x, self.initial_position[1] - 1 + pos_y])
                self
                for food in self.food_positions:
                    self._around_food.append([food[0] - 1 + pos_x, food[1] - 1 + pos_y])
                    self._grid_to_food[food[0] - 1 + pos_x, food[1] - 1 + pos_y] = 100

    @property
    def grid_to_home(self):
        with self._lock:
            return self._grid_to_home

    @grid_to_home.setter
    def grid_to_home(self, value):
        with self._lock:
            self._grid_to_home = value
            for pos_x in range(3):
                for pos_y in range(3):
                    self._grid_to_home[self.initial_position[0] - 1 + pos_x, self.initial_position[1] - 1 + pos_y] = 100
                    for food in self.food_positions:
                        self._grid_to_food[food[0] - 1 + pos_x, food[1] - 1 + pos_y] = 100
    
    @property
    def grid_to_food(self):
        with self._lock:
            return self._grid_to_food
    
    @grid_to_food.setter
    def grid_to_food(self, value):
        with self._lock:
            self._grid_to_food = value
            for pos_x in range(3):
                for pos_y in range(3):
                    self._grid_to_home[self.initial_position[0] - 1 + pos_x, self.initial_position[1] - 1 + pos_y] = 100
                    for food in self.food_positions:
                        self._grid_to_food[food[0] - 1 + pos_x, food[1] - 1 + pos_y] = 100
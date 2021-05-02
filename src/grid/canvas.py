
from singleton_decorator import singleton
from .grid import Grids
import numpy as np
from threading import Lock

@singleton
class Canvas:
    WHITE = 0
    BLACK = 1
    GREEN = 2
    PURPLE = 3
    YELLOW = 4
    RED = 5
    
    def __init__(self, shape = (30, 30)):
        self._grid: np.array = np.zeros(shape=(Grids().limit, Grids().limit))
        self._lock = Lock()
        self._grid[Grids().initial_position[0], Grids().initial_position[1]] = self.BLACK
        self._grid[Grids().food_position[0], Grids().food_position[1]] = self.GREEN

    @property
    def grid(self):
        with self._lock:
            return self._grid

    def update_ant_position(self, old_pos, new_pos, color):
        with self._lock:
            self._grid[old_pos[0], old_pos[1]] = self.WHITE
            self._grid[new_pos[0], new_pos[1]] = color

            self._grid[Grids().initial_position[0], Grids().initial_position[1]] = self.BLACK
            self._grid[Grids().food_position[0], Grids().food_position[1]] = self.GREEN

    

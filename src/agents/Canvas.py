from random import choice
from pade.core.agent import Agent
from pade.misc.utility import display_message
from pade.behaviours.protocols import TimedBehaviour
from ..grid.grid import Grids
from ..grid.canvas import Canvas
from ..settings import AGENT_TIME
import pygame
import sys

GREEN_COLOR = (0,255,0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
PURPLE_COLOR = (255,0,255)
YELLOW_COLOR = (102,102,0)
RED_COLOR = (255,0,0)


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

class CanvasAgent(Agent):
    def __init__(self, aid):
        super(CanvasAgent, self).__init__(aid=aid)
        pygame.init()
        self.size = Grids().limit * 10
        self.SCREEN = pygame.display.set_mode((self.size, self.size))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(WHITE_COLOR)
        self.behaviours.append(ComportTemporal(self, AGENT_TIME))
    
    
    def draw_grid(self):
        blockSize = 10 #Set the size of the grid block
        for index_x, x in enumerate(Canvas().grid):
            for index_y, y in enumerate(x):
                color = self.get_color_by_grid_position(y)
                if color != RED_COLOR:    
                    rect = pygame.Rect(index_x * 10, index_y * 10, blockSize, blockSize)

                    pygame.draw.rect(self.SCREEN, color, rect)
                else:
                    pygame.draw.circle(
                        self.SCREEN, 
                        RED_COLOR, 
                        ((index_x * 10) + 5, (index_y * 10) + 5), 5)         
        for index_x, x in enumerate(Grids().grid_to_home):
            for index_y, y in enumerate(x): 
                if y:
                    size = min(int(y/5) + 1, 4) if [index_x, index_y] not in Grids()._around_base else 4
                    pygame.draw.circle(
                        self.SCREEN, 
                        PURPLE_COLOR, 
                        ((index_x * 10) + 3, (index_y * 10) + 3), size) 
                        
        for index_x, x in enumerate(Grids().grid_to_food):
            for index_y, y in enumerate(x): 
                if y:
                    size = min(int(y/5) + 1, 4) if [index_x, index_y] not in Grids()._around_food else 4
                    pygame.draw.circle(
                        self.SCREEN, 
                        YELLOW_COLOR, 
                        ((index_x * 10) + 8, (index_y * 10) + 8), size)

        for index_x, x in enumerate(Canvas().grid):
            for index_y, y in enumerate(x):
                color = self.get_color_by_grid_position(y)
                if color != WHITE_COLOR:    
                    rect = pygame.Rect(index_x * 10, index_y * 10, blockSize, blockSize)

                    pygame.draw.rect(self.SCREEN, color, rect)

    def get_color_by_grid_position(self, grid_value): 
        color = WHITE_COLOR
        if (grid_value == Canvas().BLACK):
            color = BLACK_COLOR
        elif (grid_value == Canvas().GREEN):
            color = GREEN_COLOR
        elif (grid_value == Canvas().PURPLE):
            color = PURPLE_COLOR
        elif (grid_value == Canvas().RED):
            color = RED_COLOR
        elif (grid_value == Canvas().YELLOW):
            color = YELLOW_COLOR
        return color
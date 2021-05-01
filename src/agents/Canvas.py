from random import choice
from pade.core.agent import Agent
from pade.misc.utility import display_message
from pade.behaviours.protocols import TimedBehaviour
import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

class CanvasAgent(Agent):
    def __init__(self, aid):
        super(CanvasAgent, self).__init__(aid=aid)
        pygame.init()
        self.SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(BLACK)

        self.behaviours.append(ComportTemporal(self, .1))
    
    
    def drawGrid(self):
        blockSize = 20 #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.SCREEN, WHITE, rect, 1)


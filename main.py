from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from src.agents.Canvas import CanvasAgent
from src.agents.Ant import Ant
from src.agents.Environment import EnvironmentAgent
from src.grid.grid import Grids
from sys import argv
import numpy as np
import pygame


if __name__ == '__main__':

    agents_per_process = 30
    agents = []

    c = 0

    for i in range(agents_per_process):
        port = int(argv[1]) + c
        agent_name = f'Ant_{i}'

        ant = Ant(AID(name=agent_name), current_pos = Grids().initial_position)

        agents.append(ant)
        c += 2

    agents.append(CanvasAgent(AID(name="Canvas_Agent")))
    agents.append(EnvironmentAgent(AID(name="Environment_Agent")))

    start_loop(agents)


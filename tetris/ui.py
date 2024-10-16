import pygame
from pygame.locals import *
from config import SCREEN_HEIGHT, SCREEN_WIDTH

class UI():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

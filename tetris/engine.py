import pygame
from pygame.locals import *
import random
import models
from config import GRID_WIDTH, GRID_HEIGHT

class Engine():
    """All basic calculations and services are performed here. This class contains the main game loop, controls the changing of the piece coordinates
    and tracks the piece collisions."""
    def __init__(self,ui):
        self.screen_matrix = self.build_matrix()
        self.ui = ui
        self.clock = pygame.time.Clock()

    def build_matrix(self) -> list[list[list]]:
        # build collision tracking matrix
        matrix = [[[None,None] for i in range(GRID_WIDTH)] for x in range(GRID_HEIGHT)]
        return matrix
    
    def try_move_piece(self, direction: tuple, piece: models.Tetromino) -> bool:
        # check if a piece can be moved in a certain direction
        pass

    def try_rotate_piece(self, direction: int, piece: models.Tetromino) -> bool:
        # check if a piece can be rotated in a certian direction
        pass

    def commit_piece_to_matrix(self, piece: models.Tetromino):
        # add the piece to the game matrix
        pass

    def check_row_completion(self):
        # check if a row is completed in the matrix
        pass
    
    def clear_row(self):
        # clear the completed row and drop exising occupied spaces to fill previous row, add new row to beginning of matrix
        pass
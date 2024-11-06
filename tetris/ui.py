import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BOX_WIDTH, BOX_HEIGHT

class UI():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # update screen functions
    def update_screen(self, matrix, piece):
        self.clear_screen()
        self.draw_static_rect(matrix)
        self.draw_current_piece(piece)
        pygame.display.update()

    # 'clear' the screen by filling it with black
    def clear_screen(self):
        self.screen.fill((0,0,0))

    # draw all static rect's, takes a maxtrix of objects or none, draws objects if they are there
    def draw_static_rect(self,matrix: list[list]):
        for row_num,row in enumerate(matrix):
            for col_num,cell in enumerate(row):
                if cell[0] is not None:
                    rectangle = pygame.Rect(col_num * BOX_WIDTH, row_num * BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)
                    pygame.draw.rect(self.screen, cell[1], rectangle)
                   

    # draw moving piece
    def draw_current_piece(self,piece):
        
        for coord in piece.get_grid_coordinates(piece.shape):
            rect = pygame.Rect(coord[0]*BOX_WIDTH, coord[1]*BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)
            pygame.draw.rect(self.screen, piece.color ,rect)
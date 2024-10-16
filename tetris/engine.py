import pygame
from pygame.locals import *
import random
import models
from config import GRID_WIDTH, GRID_HEIGHT, FRAMERATE, SPEED

class Engine():
    def __init__(self,ui):
        self.screen_matrix = self.build_matrix()
        self.ui = ui
        self.clock = pygame.time.Clock()
    
    # build collision tracking matrix
    def build_matrix(self):
        matrix = [[None for i in range(GRID_WIDTH)] for x in range(GRID_HEIGHT)]
        return matrix
    
    # add a static piece to the matrix
    def add_piece_to_matrix(self):
        pass
    
    # check if a row is completed in the matrix
    def check_row_completion(self):
        pass
    
    # clear the completed row and drop exising occupied spaces to fill previous row, add new row to beginning of matrix
    def clear_row(self):
        pass

    # main game loop
    def run(self):
        run = True
        piece = self.get_new_piece()
   
        moving_piece = True
        num_frames = 0
        while run:
            
            # set the framerate first
            self.clock.tick(FRAMERATE)

            # check if a new piece is needed
            if moving_piece == False:
                piece = self.get_new_piece()

            # check if the piece needs to move down
            if num_frames == SPEED:
                piece.move_down()
                num_frames = 0
            else:
                num_frames += 1
                
            self.ui.update_screen(self.screen_matrix, piece)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

    # get random tetromino to use
    def get_new_piece(self):
        piece_num = random.randrange(1,8)
        match piece_num:
            case 1:
                return models.Line(0,0)
            case 2:
                return models.T(0,0)
            case 3:
                return models.L(0,0)
            case 4:
                return models.J(0,0)
            case 5:
                return models.S(0,0)
            case 6:
                return models.Z(0,0)
            case 7:
                return models.Square(0,0)
            
    


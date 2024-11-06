"""This is the main engine module, handling the game loop and """
import pygame
from pygame.locals import *
import random
import models
import config

class Engine():
    """All basic calculations and services are performed here. This class contains the main game loop, controls the changing of the piece coordinates
    and tracks the piece collisions."""
    def __init__(self,ui):
        self.screen_grid = self.build_matrix()
        self.ui = ui
        self.clock = pygame.time.Clock()

    def build_matrix(self) -> list[list[list]]:
        # build collision tracking matrix
        matrix = [[[None,None] for i in range(config.GRID_WIDTH)] for x in range(config.GRID_HEIGHT)]
        return matrix
    
    def get_new_piece(self) -> models.Tetromino:
         # get random tetromino to use
        piece_num = random.randrange(1,8)
        match piece_num:
            case 1:
                return models.Line()
            case 2:
                return models.T()
            case 3:
                return models.L()
            case 4:
                return models.J()
            case 5:
                return models.S()
            case 6:
                return models.Z()
            case 7:
                return models.Square()
    
    def try_move_piece(self, direction: tuple, piece: models.Tetromino) -> bool:
        # check if a piece can be moved in a certain direction
        piece_coords = piece.get_grid_coordinates()
        for coord in piece_coords:
            row = coord[1] + direction[1]
            col = coord[0] + direction[0]
            if row >= 0 and row < config.GRID_HEIGHT and col >= 0 and col < config.GRID_WIDTH:
                if self.screen_grid[row][col][0] == 1:
                    return False
            else:
                return False
        return True

    def try_rotate_piece(self, direction: int, piece: models.Tetromino) -> bool:
        # check if a piece can be rotated in a certian direction
        pass

    def commit_piece_to_matrix(self, piece: models.Tetromino):
        # add the piece to the game grid
        pass

    def check_row_completion(self):
        # check if a row is completed in the grid
        pass
    
    def clear_row(self):
        # clear the completed row and drop exising occupied spaces to fill previous row, add new row to beginning of grid
        pass

        # move or rotate piece as needed
    def event_actions(self, event, piece):
        key = event.key
        match key:
            case pygame.K_d: #right movement of piece
                piece.potential_right()
                if self.check_movement_collision(piece) is False:
                    piece.commit_coordinates()
            case pygame.K_a: #left movement of piece
                piece.potential_left()
                if self.check_movement_collision(piece) is False:
                    piece.commit_coordinates()
            case pygame.K_s: #increased fall movement of piece
                pass
            case pygame.K_RIGHT: #right turn of piece
                piece.turn_right()
                if self.check_movement_collision(piece) is False:
                    piece.commit_coordinates()
            case pygame.K_LEFT: #left turn of piece
                piece.turn_left()
                if self.check_movement_collision(piece) is False:
                    piece.commit_coordinates()

    def game_loop(self):
        # main game loop
        running = True

        #get initial piece and states piece is moving
        piece = self.get_new_piece()
        moving_piece = True

        #initialize frame counter
        frame_count = 0

        while running:

            #set game tick rate
            self.clock.tick(config.FPS)

            # check if a new piece is needed using moving_piece
            if moving_piece == False:
                piece = self.get_new_piece()
                moving_piece = True

            #gets the keypress and passes it to the actions function
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.event_actions(event, piece)
                if event.type == pygame.QUIT:
                    run = False

            #check fall speed and move piece as needed
            if frame_count == (config.FPS/config.FALL_SPEED):
                if self.try_move_piece((0,1), piece):
                    piece.commit_move((0,1))

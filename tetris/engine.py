import pygame
from pygame.locals import *
import random
import models
from config import GRID_WIDTH, GRID_HEIGHT, FRAMERATE, DROP_TIMING, SIDE_STEP

class Engine():
    """All basic calculations and services are performed here. This class contains the main game loop, controls the changing of the piece coordinates
    and tracks the piece collisions."""
    def __init__(self,ui):
        self.screen_matrix = self.build_matrix()
        self.ui = ui
        self.clock = pygame.time.Clock()
    
    # build collision tracking matrix
    def build_matrix(self):
        matrix = [[[None,None] for i in range(GRID_WIDTH)] for x in range(GRID_HEIGHT)]
        return matrix
    
    # check for collision while falling. It will predict where the piece will fall and check there before allowing it to be drawn
    def check_fall_collision(self,piece):
        for coord in piece.coords:
            grid_row = int(coord[0])
            if coord[0] % SIDE_STEP == 0:
                grid_col = int(coord[1])
                if grid_row +1  == GRID_HEIGHT or self.screen_matrix[grid_row+1][grid_col][0]:

                    return True
        return False

    #check for collision when moving the piece
    def check_movement_collision(self,piece):
        for coord in piece.potential_coords:
            grid_row = int(coord[0])
            grid_col = int(coord[1])
            if grid_col < 0 or grid_col > GRID_WIDTH - 1 or self.screen_matrix[grid_row][grid_col][0] is not None:
                return True
        return False

    # add a static piece to the matrix
    def add_piece_to_matrix(self,piece):
        for coord in piece.coords:
            grid_row = int(coord[0])
            grid_col = int(coord[1])
            self.screen_matrix[grid_row][grid_col][0] = 1
        return False
    
    # check if a row is completed in the matrix
    def check_row_completion(self):
        pass
    
    # clear the completed row and drop exising occupied spaces to fill previous row, add new row to beginning of matrix
    def clear_row(self):
        pass

    # main game loop
    def run(self):
        run = True
        # piece = self.get_new_piece()
        piece = self.get_new_piece()
   
        moving_piece = True #indicates that a piece is falling. 
        num_frames = 0 #initialize the number of frames, used in falling speed
        while run:
            
            # set the framerate first
            self.clock.tick(FRAMERATE)

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

            # check if the piece needs to move down
            if num_frames == DROP_TIMING:
                if not self.check_fall_collision(piece):
                    piece.move_down()
                    num_frames = 0
                else:
                    if not self.add_piece_to_matrix(piece): #if a piece stops falling, it sets moving_piece to false to call a new piece
                        moving_piece = False
            else:
                num_frames += 1

            self.ui.update_screen(self.screen_matrix, piece)# passing the matrix and piece to the ui to be drawn
                

    # get random tetromino to use
    def get_new_piece(self):
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
                pass
            case pygame.K_LEFT: #left turn of piece
                pass

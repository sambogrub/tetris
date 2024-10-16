import pygame
from pygame.locals import *
import random
from models import Square, Line, L, J, S, Z, T
from config import RECT_WIDTH, RECT_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED, SIDE_STEP, GRID_HEIGHT, GRID_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

step = SIDE_STEP
player = Line(0, 0)

# grid = []

# for y in range(20):
#     x_grid = []
#     for x in range(10):
#         xpos = x*RECT_HEIGHT
#         ypos = y*RECT_WIDTH
#         grid_square = pygame.Rect((xpos,ypos,RECT_WIDTH,RECT_HEIGHT))
#         x_grid.append(grid_square)
#     grid.append(x_grid)
        
screen_matrix = [[0 for i in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]


def get_piece_coords(piece):
    coords = []
    for rect in piece:
        p_col = rect.x // step
        p_row = rect.y // step
        coords.append((p_row, p_col))
    return coords

def is_collision(coords, matrix):
    for (row,col) in coords:
        print(row,col)
        if col < 0 or col >= GRID_WIDTH or row + 1 >= GRID_HEIGHT:
            return True
        if matrix[row][col] != 0:
            return True
    return False

screen_matrix[19][0] = 1
screen_matrix[19][1] = 1
screen_matrix[19][2] = 1
screen_matrix[19][3] = 1

clock = pygame.time.Clock()

move = 0

run = True
while run:
    clock.tick(60)
    
    screen.fill((0,0,0))

    # for x_grid in grid:
    #     for square in x_grid:
    #         pygame.draw.rect(screen, (250,250,250),square,1)

    


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right()
                player_coords =get_piece_coords(player)
                if is_collision(player_coords,screen_matrix):
                    player.move_left()
            elif event.key == pygame.K_a:
                player.move_left()
                player_coords =get_piece_coords(player)
                if is_collision(player_coords,screen_matrix):
                    player.move_right()
            elif event.key == pygame.K_w:
                player.turn_right()
                
        
            
       
        if event.type == pygame.QUIT:
            run = False

    for rect in player:
        pygame.draw.rect(screen, (255,0,0),rect)

    
    if move == SPEED:
        player_coords= get_piece_coords(player)
        if is_collision(player_coords,screen_matrix) == False:
            player.move_down()
            move = 0
        else:
            for (row,col) in player_coords:
                screen_matrix[row][col] = 1
    else:    
        move +=1

    pygame.display.update()




print(screen_matrix)
pygame.quit()
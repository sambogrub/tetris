import pygame
from pygame.locals import *
import random
from models import Square, Line, L, J, S, Z, T
from config import RECT_WIDTH, RECT_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


player = T(0, 0)

grid = []

# for y in range(20):
#     x_grid = []
#     for x in range(10):
#         xpos = x*RECT_HEIGHT
#         ypos = y*RECT_WIDTH
#         grid_square = pygame.Rect((xpos,ypos,RECT_WIDTH,RECT_HEIGHT))
#         x_grid.append(grid_square)
#     grid.append(x_grid)
        


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
            elif event.key == pygame.K_a:
                player.move_left()
                
        
            
       
        if event.type == pygame.QUIT:
            run = False

    for rect in player:
        pygame.draw.rect(screen, (255,0,0),rect)
    if move == SPEED:
        player.move_down()
        move = 0
    else:    
        move +=1

    pygame.display.update()
pygame.quit()
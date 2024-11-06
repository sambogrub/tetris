import pygame
from pygame.locals import *
from engine import Engine
from ui import UI

def main():
    # initialize the pygame environment
    pygame.init()
    
    # initialize the parts of the game
    ui = UI()
    engine = Engine(ui)

    #start the game
    engine.game_loop()

    # quit when the run loop ends
    pygame.quit()

if __name__ == '__main__':
    main()

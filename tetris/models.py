import pygame
from config import RECT_HEIGHT, RECT_WIDTH, SIDE_STEP, FALL_STEP


class Tetromino:
    def __init__(self):
        self.step = SIDE_STEP
        self.fall_step = FALL_STEP
        self._index = 0
        self.shape = []

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self.shape):
            result = self.shape[self._index]
            self._index += 1
            return result
        else:
            self._index = 0
            raise StopIteration
        
    def move_left(self):
        for rect in self.shape:
            rect.x -= self.step

    def move_right(self):
        for rect in self.shape:
            rect.x += self.step

    def move_down(self):
        for rect in self.shape:
            rect.y += self.fall_step

class Square(Tetromino):
    def __init__(self,xpos,ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)
        

    def build_shape(self, xpos, ypos) -> list:
        top_l = pygame.Rect(xpos, ypos, self.width, self.height)
        top_r = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        bot_l = pygame.Rect(xpos, ypos+self.step, self.width, self.height)
        bot_r = pygame.Rect(xpos +self.step, ypos+self.step, self.width, self.height)
        shape = [top_l,top_r,bot_l,bot_r]
        return shape


class Line(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos, ypos, self.width, self.height)
        second = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        third = pygame.Rect(xpos+(self.step*2), ypos, self.width, self.height)
        fourth = pygame.Rect(xpos+(self.step*3), ypos, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape

class Tee(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos, ypos, self.width, self.height)
        second = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        third = pygame.Rect(xpos+(self.step*2), ypos, self.width, self.height)
        fourth = pygame.Rect(xpos+self.step, ypos+self.step, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape
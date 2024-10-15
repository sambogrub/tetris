import pygame
from config import RECT_HEIGHT, RECT_WIDTH, SIDE_STEP, FALL_STEP

# base tetromino class
class Tetromino:
    def __init__(self):
        self.step = SIDE_STEP
        self.fall_step = FALL_STEP
        self._index = 0
        self.shape = []
        self.orientation = 0

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

# square shaped tetromino
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

# line shaped tetromino
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
    

    def orientation_0(self):
        self.shape[0] = self.shape[0].move(self.step * -2, self.step)
        self.shape[1] = self.shape[1].move(-self.step, 0)
        self.shape[2] = self.shape[2].move(0, -self.step)
        self.shape[3] = self.shape[3].move(self.step, self.step * -2)

    def orientation_1(self):
        self.shape[0] = self.shape[0].move(self.step * 2, -self.step)
        self.shape[1] = self.shape[1].move(self.step, 0)
        self.shape[2] = self.shape[2].move(0, self.step)
        self.shape[3] = self.shape[3].move(-self.step, self.step * 2)


    def turn_right(self) -> list:
        if self.orientation == 0:
            self.orientation_1()
            self.orientation = 1
        elif self.orientation == 1:
            self.orientation_0()
            self.orientation = 0

        


# t shaped tetromino
class T(Tetromino):
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
    
# l shaped tetromino
class L(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos, ypos, self.width, self.height)
        second = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        third = pygame.Rect(xpos+(self.step*2), ypos, self.width, self.height)
        fourth = pygame.Rect(xpos, ypos+self.step, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape
    
# j shaped tetromino
class J(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos, ypos, self.width, self.height)
        second = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        third = pygame.Rect(xpos+(self.step*2), ypos, self.width, self.height)
        fourth = pygame.Rect(xpos+(self.step*2), ypos+self.step, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape
    
# s shaped tetromino
class S(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        second = pygame.Rect(xpos+(self.step*2), ypos, self.width, self.height)
        third = pygame.Rect(xpos, ypos+self.step, self.width, self.height)
        fourth = pygame.Rect(xpos+self.step, ypos+self.step, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape
    
# z shaped tetromino
class Z(Tetromino):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.shape = self.build_shape(xpos, ypos)

    def build_shape(self, xpos, ypos) -> list:
        first = pygame.Rect(xpos, ypos, self.width, self.height)
        second = pygame.Rect(xpos+self.step, ypos, self.width, self.height)
        third = pygame.Rect(xpos+self.step, ypos+self.step, self.width, self.height)
        fourth = pygame.Rect(xpos+(self.step*2), ypos+self.step, self.width, self.height)
        shape = [first, second, third, fourth]
        return shape
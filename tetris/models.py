import pygame
from config import RECT_HEIGHT, RECT_WIDTH, SIDE_STEP, FALL_STEP

# base tetromino class
class Tetromino:
    def __init__(self):
        self.step = SIDE_STEP
        self.fall_step = FALL_STEP
        self.coords = []
        self.color = (255,0,0)
        self.orientation = 0
        
    def move_left(self):
        for coord in self.coords:
            coord[1] -= self.step

    def move_right(self):
        for coord in self.coords:
            coord[1] += self.step

    def move_down(self):
        for coord in self.coords:
            coord[0] += self.fall_step

# square shaped tetromino
class Square(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    # retruns a list of lists -> [[row,col],[row,col],[row,col],[row,col]]    
    def build_shape(self) -> list[list]:
        top_l = [0.0,0.0]
        top_r = [0.0,1.0]
        bot_l = [1.0,0.0]
        bot_r = [1.0,1.0]
        coords = [top_l,top_r,bot_l,bot_r]
        return coords
    
    def turn_right(self):
        pass
    
    def turn_left(self):
        pass

# line shaped tetromino
class Line(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,0.0]
        second = [0.0,1.0]
        third = [0.0,2.0]
        fourth = [0.0,3.0]
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

    def turn_left(self) -> list:
        if self.orientation == 0:
            self.orientation_1()
            self.orientation = 1
        elif self.orientation == 1:
            self.orientation_0()
            self.orientation = 0
        


# t shaped tetromino
class T(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,0.0]
        second = [0.0,1.0]
        third = [0.0,2.0]
        fourth = [1.0,1.0]
        shape = [first, second, third, fourth]
        return shape
    
# l shaped tetromino
class L(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,0.0]
        second = [0.0,1.0]
        third = [0.0,2.0]
        fourth = [1.0,0.0]
        shape = [first, second, third, fourth]
        return shape
    
# j shaped tetromino
class J(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,0.0]
        second = [0.0,1.0]
        third = [0.0,2.0]
        fourth = [1.0,2.0]
        shape = [first, second, third, fourth]
        return shape
    
# s shaped tetromino
class S(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,1.0]
        second = [0.0,2.0]
        third = [1.0,0.0]
        fourth = [1.0,1.0]
        shape = [first, second, third, fourth]
        return shape
    
# z shaped tetromino
class Z(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = RECT_WIDTH
        self.height = RECT_HEIGHT
        self.coords = self.build_shape()

    def build_shape(self) -> list:
        first = [0.0,0.0]
        second = [0.0,1.0]
        third = [1.0,1.0]
        fourth = [1.0,2.0]
        shape = [first, second, third, fourth]
        return shape
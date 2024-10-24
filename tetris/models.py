import pygame
from config import RECT_HEIGHT, RECT_WIDTH, SIDE_STEP, FALL_STEP


# base tetromino class
class Tetromino:
    """This is the parent Tetromino class containing all the basic movements for each piece.
    Each individual piece will contain its own rotation functions"""
    def __init__(self):
        self.step = SIDE_STEP
        self.fall_step = FALL_STEP
        self.coords = []
        self.potential_coords = []
        self.color = (255,0,0)
        self.orientation = 0

    #setting the potential coordinates for moving left to find possible collisions  
    def potential_left(self):
        self.potential_coords = [coord[:] for coord in self.coords]
        for coord in self.potential_coords:
            coord[1] -= self.step
        
    # setting the potential coordinates for moving right to find possible collisions
    def potential_right(self):
        self.potential_coords = [coord[:] for coord in self.coords]
        for coord in self.potential_coords:
            coord[1] += self.step
        
    # commit the potential coordinates to the actual coordinates
    def commit_coordinates(self):
        self.coords = [coord[:] for coord in self.potential_coords]

    # move down function
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
        top_l = [0,0]
        top_r = [0,1]
        bot_l = [1,0]
        bot_r = [1,1]
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
        first = [0,0]
        second = [0,1]
        third = [0,2]
        fourth = [0,3]
        shape = [first, second, third, fourth]
        return shape
    
    def orientation_0(self):
        pass

    def orientation_1(self):
        pass

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
        first = [0,0]
        second = [0,1]
        third = [0,2]
        fourth = [1,1]
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
        first = [0,0]
        second = [0,1]
        third = [0,2]
        fourth = [1,0]
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
        first = [0,0]
        second = [0,1]
        third = [0,2]
        fourth = [1,2]
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
        first = [0,1]
        second = [0,2]
        third = [1,0]
        fourth = [1,1]
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
        first = [0,0]
        second = [0,1]
        third = [1,1]
        fourth = [1,2]
        shape = [first, second, third, fourth]
        return shape
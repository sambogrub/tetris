import pygame
from config import BOX_HEIGHT, BOX_WIDTH, SIDE_STEP, FALL_STEP, BOX_DIVISION


# base tetromino class
class Tetromino:
    """This is the parent Tetromino class containing all the basic movements for each piece.
    Each individual piece will contain its own rotation functions"""
    def __init__(self):
        self.step = SIDE_STEP
        self.fall_step = FALL_STEP
        # self.shape = []
        self.coords = []
        self.potential_coords = []
        self.color = (255,255,255)
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

    # def pop_coords(self):
    #     coords = []
    #     for rect in self.shape:
    #         coord = []
    #         for i in range(BOX_DIVISION):
    #             new_row = rect[0] * i
    #             new_col = rect[1] * i
    #             coord.append([new_row,new_col])




# square shaped tetromino
class Square(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (255,0,0)

    # retruns a list of lists -> [[row,col],[row,col],[row,col],[row,col]]    
    def build_shape(self) -> list[list]:
        top_l = [0*BOX_DIVISION,0*BOX_DIVISION]
        top_r = [0*BOX_DIVISION,1*BOX_DIVISION]
        bot_l = [1*BOX_DIVISION,0*BOX_DIVISION]
        bot_r = [1*BOX_DIVISION,1*BOX_DIVISION]
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
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (0,0,255)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,0*BOX_DIVISION]
        second = [0*BOX_DIVISION,1*BOX_DIVISION]
        third = [0*BOX_DIVISION,2*BOX_DIVISION]
        fourth = [0*BOX_DIVISION,3*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
    
    def orientation_0(self):
       
        self.potential_coords = [coord[:] for coord in self.coords]
        self.potential_coords[0] = [self.potential_coords[0][0]-1*BOX_DIVISION,
                                    self.potential_coords[0][1]+2*BOX_DIVISION]
        self.potential_coords[1] = [self.potential_coords[1][0]+1*BOX_DIVISION,
                                    self.potential_coords[1][1]+1*BOX_DIVISION]
        self.potential_coords[3] = [self.potential_coords[3][0]+2*BOX_DIVISION,
                                    self.potential_coords[3][1]-1*BOX_DIVISION]
        
        self.orientation = 0
      

    def orientation_1(self):
       
        self.potential_coords = [coord[:] for coord in self.coords]
        self.potential_coords[0] = [self.potential_coords[0][0]+1*BOX_DIVISION,
                                    self.potential_coords[0][1]-2*BOX_DIVISION]
        self.potential_coords[1] = [self.potential_coords[1][0]-1*BOX_DIVISION,
                                    self.potential_coords[1][1]-1*BOX_DIVISION]
        self.potential_coords[3] = [self.potential_coords[3][0]-2*BOX_DIVISION,
                                    self.potential_coords[3][1]+1*BOX_DIVISION]
        self.orientation = 1
  

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
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (0,255,0)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,0*BOX_DIVISION]
        second = [0*BOX_DIVISION,1*BOX_DIVISION]
        third = [0*BOX_DIVISION,2*BOX_DIVISION]
        fourth = [1*BOX_DIVISION,1*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
    

# l shaped tetromino
class L(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (255,255,0)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,0*BOX_DIVISION]
        second = [0*BOX_DIVISION,1*BOX_DIVISION]
        third = [0*BOX_DIVISION,2*BOX_DIVISION]
        fourth = [1*BOX_DIVISION,0*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
    

# j shaped tetromino
class J(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (0,255,255)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,0*BOX_DIVISION]
        second = [0*BOX_DIVISION,1*BOX_DIVISION]
        third = [0*BOX_DIVISION,2*BOX_DIVISION]
        fourth = [1*BOX_DIVISION,2*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
    

# s shaped tetromino
class S(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (255,0,255)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,1*BOX_DIVISION]
        second = [0*BOX_DIVISION,2*BOX_DIVISION]
        third = [1*BOX_DIVISION,0*BOX_DIVISION]
        fourth = [1*BOX_DIVISION,1*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
    

# z shaped tetromino
class Z(Tetromino):
    def __init__(self):
        super().__init__()
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.coords = self.build_shape()
        self.color = (255,255,255)

    def build_shape(self) -> list:
        first = [0*BOX_DIVISION,0*BOX_DIVISION]
        second = [0*BOX_DIVISION,1*BOX_DIVISION]
        third = [1*BOX_DIVISION,1*BOX_DIVISION]
        fourth = [1*BOX_DIVISION,2*BOX_DIVISION]
        shape = [first, second, third, fourth]
        return shape
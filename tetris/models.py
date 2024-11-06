"""This module holds the indiviual pieces. Each piece will contain it's own
shape coordinates, as well as the conversion to grid coordinates"""
import config


class Tetromino:
    """This is the base tetromino class. the pieces will inherit basic movment from this class"""
    def __init__(self):
        self.shape = []
        self.coordinates = []
        self.color = (255,0,0)
        self.orientation = 0
        self.x_offset = 0
        self.y_offset = 0

    def get_grid_coordinates(self, shape_) -> list:
        #sets shape to actual coordinates for the grid
        new_coords = []
        for r, row in enumerate(shape_):
            for c, col in enumerate(row):
                if col == 1:
                    x = c + self.x_offset
                    y = r + self.y_offset
                    new_coords.append((x,y))
        return new_coords

    def commit_move(self, direction: tuple):
        self.x_offset += direction[0]
        self.y_offset += direction[1]

    def turn_count_clock(self):
        self.shape = list(zip(*self.shape))[::-1]

    def turn_clock(self):
        self.shape = list(zip(*self.shape[::-1]))

    
class Line(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (0,0,255)

    def build_shape(self) -> list:
        shape = [[1,1,1,1]]
        return shape


class Square(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (255,0,0)

    def build_shape(self) -> list:
        shape = [[1,1],
                 [1,1]]
        return shape


class T(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (0,255,0)

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [0,1,0]]
        return shape


class S(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (255,0,255)

    def build_shape(self) -> list:
        shape = [[0,1,1],
                 [1,1,0]]
        return shape


class Z(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (255,255,255)

    def build_shape(self) -> list:
        shape =[[1,1,0],
                [0,1,1]]
        return shape


class L(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (255,255,0)

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [1,0,0]]
        return shape


class J(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()
        self.color = (0,255,255)

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [0,0,1]]
        return shape
    
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

    def get_grid_coordinates(self) -> list:
        #sets shape to actual coordinates for the grid
        new_coords = []
        for r, row in enumerate(self.shape):
            for c, col in enumerate(row):
                if col == 1:
                    x = c + self.x_offset
                    y = r + self.y_offset
                    new_coords.append((x,y))
        return new_coords

    def get_possible_coordinates(self, direction: tuple) -> list:
        new_coords = []
        for r, row in enumerate(self.shape):
            for c, col in enumerate(row):
                if col == 1:
                    x = c + self.x_offset + direction[0]
                    y = r + self.y_offset + direction[1]
                    new_coords.append((x,y))
        return new_coords

    def try_move(self, direction: tuple, grid: list[list[list]]):
        coords = self.get_grid_coordinates()
        for coord in coords:
            row = coord[1] + direction[1]
            col = coord[0] + direction[0]
            if row >= 0 and row < config.GRID_HEIGHT and col >= 0 and col < config.GRID_WIDTH:
                if grid[row][col][0] == 1:
                    return False
            else:
                return False
        return True
    
    def commit_move(self, direction: tuple):
        self.x_offset += direction[0]
        self.y_offset += direction[1]

    
class Line(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[1,1,1,1]]
        return shape


class Square(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[1,1],
                 [1,1]]
        return shape


class T(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [0,1,0]]
        return shape


class S(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,1,1],
                 [1,1,0]]
        return shape


class Z(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape =[[1,1,0],
                [0,1,1]]
        return shape


class L(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [1,0,0]]
        return shape


class J(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[1,1,1],
                 [0,0,1]]
        return shape
    
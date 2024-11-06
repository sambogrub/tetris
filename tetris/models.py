"""This module holds the indiviual pieces. Each piece will contain it's own
shape coordinates, as well as the conversion to grid coordinates"""
import config


class Tetromino:
    """This is the base tetromino class. the pieces will inherit basic movment from this class"""
    def __init__(self):
        self.shape = []
        self.coordinates = []
        self.color = (255,0,0)
        self.x_offset = 0
        self.y_offset = 0

    def piece_down(self):
        pass

    def piece_left(self):
        pass

    def piece_right(self):
        pass
    


class Line(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class Square(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class T(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class S(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class Z(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class L(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape


class J(Tetromino):
    def __init__(self):
        super().__init__()
        self.shape = self.build_shape()

    def build_shape(self) -> list:
        shape = [[0,0],[1,0],[2,0],[3,0]]
        return shape
    
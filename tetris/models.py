import pygame


class Tetromino:
    def __init__(self, step):
        self.step = step
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
            rect.y += self.step/5

class Square(Tetromino):
    def __init__(self,xpos,ypos,width,height,step):
        super().__init__(step)
        self.shape = self.build_shape(xpos, ypos, width, height)
        



    # def __iter__(self):
    #     return self
    
    # def __next__(self):
    #     if self._index < len(self.square):
    #         result = self.square[self._index]
    #         self._index += 1
    #         return result
    #     else:
    #         self._index = 0
    #         raise StopIteration

    def build_shape(self, xpos, ypos, width, height) -> list:
        top_l = pygame.Rect(xpos, ypos, width, height)
        top_r = pygame.Rect(xpos+self.step, ypos, width, height)
        bot_l = pygame.Rect(xpos, ypos+self.step, width, height)
        bot_r = pygame.Rect(xpos +self.step, ypos+self.step, width, height)
        shape = [top_l,top_r,bot_l,bot_r]
        return shape



    # def move_left(self):
    #     for rect in self.square:
    #         rect.x += -self.step

    # def move_right(self):
    #     for rect in self.square:
    #         rect.x += self.step

    # def turn_right(self):
    #     pass

    # def turn_left(self):
    #     pass

# class Line:

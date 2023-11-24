import pygame

class Piece:

    def __init__(self, row, column, color, isKing = False):
        self.row = row 
        self.column = column
        self.x = 37.5 + (75 * column)
        self.y = 37.5 + (75 * row)
        self.color = color 
        self.isKing = isKing
    
    def set_row(self, r):
        self.row = r 
        self.y = 37.5 + (75 * self.row)

    def set_column(self, c):
        self.column = c
        self.x = 37.5 + (75 * self.column)

    def set_color(self, color):
        """ color should be an RGB tuple """
        self.color = color 
    
    def make_king(self):
        self.isKing = True
    
    def draw_piece(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 25) 
    
pygame.init()
dimension = 600

screen = pygame.display.set_mode((dimension, dimension))
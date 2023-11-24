import pygame

class Node:
    
    def __init__(self, row, column, color):
        """ Note: color should be a RGB tuple"""
        self.row = row
        self.column = column 
        self.color = color 

        self.rect = pygame.Rect(75 * row, 75 * column, 75, 75)

    def draw_cell(self):
        pygame.draw.rect(screen, self.color, self.rect)

pygame.init()
dimension = 600

screen = pygame.display.set_mode((dimension, dimension))
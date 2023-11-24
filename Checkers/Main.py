import pygame
from Board import *
from Node import *
from Piece import *

pygame.init()
dimension = 600

screen = pygame.display.set_mode((dimension, dimension))

class Main:

    def __init__(self):
        self.board = Board()
        self.isWhiteTurn = True 
        self.play_game()

    def play_game(self):

        piece_pressed = False
        emptySquare_pressed = False 

        a = None
        self.board = Board()

        while True:
            
            screen.fill((0, 0, 0))

            empty_i, empty_j = None, None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break 
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # check if the square contains a piece
                    coordx, coordy = pygame.mouse.get_pos()
                    # first, determine the column and the row that the click happened in 
                    i, j = coordx//75, coordy//75
                    
                    pressedEmpty = True  
                    for piece in self.board.pieces:
                        if piece.column == i and piece.row == j:
                            piece_pressed = True 
                            pressedEmpty = False
                            a = piece

                    if pressedEmpty:
                        empty_i, empty_j = i, j
                        emptySquare_pressed = True 

            
            if piece_pressed:
                if emptySquare_pressed:
                    oldcol, oldrow = a.column, a.row
                    if self.board.isValidMove((oldcol, oldrow), (empty_i, empty_j)):
                        a.set_row(empty_j)
                        a.set_column(empty_i)
                        self.board.pieceJumped((oldcol, oldrow), (empty_i, empty_j))
                        self.board.kingify((empty_i, empty_j))
                
            self.board.draw_board()   
            pygame.display.update()
            
            if piece_pressed and emptySquare_pressed:
                piece_pressed = False 
                emptySquare_pressed = False
        
        
if __name__ == "__main__":
    m = Main()
    #m.play_game()
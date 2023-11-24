from Piece import *
from Node import *

class Board:

    def __init__(self):
        self.board = []
        self.pieces = []
        self.construct_board()

    def construct_board(self):
        
        for i in range(8):
            for j in range(8):
                node = Node(i, j, (0, 100, 0))
                self.board.append(node)

                if (i + j) % 2 == 0 and i <= 2:
                    piece = Piece(i, j, (255, 255, 255))
                    self.pieces.append(piece)
                elif (i + j) % 2 == 0 and i >= 5:
                    piece = Piece(i, j, (200, 0, 0))
                    self.pieces.append(piece)

        for i in range(len(self.board)):
            node = self.board[i]
            if (node.row + node.column) % 2 == 1:
                node.color = (255, 255, 255)

    def draw_board(self):
        for node in self.board:
            node.draw_cell()
        for piece in self.pieces:
            piece.draw_piece()
    
    def isSquareEmpty(self, coord):
        i, j = coord[0], coord[1]
        for piece in self.pieces:
            if piece.column == i and piece.row == j:
                return False 
        return True

    def getPiece(self, coord):
        p, r = coord[0], coord[1]
        pc = None 
        for piece in self.pieces:
            if piece.column == p and piece.row == r:
                pc = piece
        return pc

    def pieceJumped(self, oldcoord, newcoord):
        i, j = oldcoord[0], oldcoord[1]
        p, r = newcoord[0], newcoord[1]
        middle_col, middle_row = (i + p)//2, (j + r)//2

        pc = self.getPiece(newcoord)
        
        if abs(i - p) == 2 and abs(j - r) == 2:
            for piece in self.pieces:
                if piece.column == middle_col and piece.row == middle_row and piece.color != pc.color:
                    self.pieces.remove(piece)
    
    def isValidMove(self, oldcoord, newcoord): 
        pc = self.getPiece(oldcoord)
        if pc is None:
            return False 

        if not pc.isKing:
            return self.isValidMoveNormal(oldcoord, newcoord)
        else:
            return self.isValidMoveNormal(oldcoord, newcoord, True)

    def isValidMoveNormal(self, oldcoord, newcoord, isKing = False):
        """ p is the piece on the oldcoord"""
        i, j = oldcoord[0], oldcoord[1]
        p, r = newcoord[0], newcoord[1]

        if i is None or j is None or p is None or r is None:
            return False 

        pc = self.getPiece(oldcoord)
        color = pc.color

        middle_col, middle_row = (i + p)//2, (j + r)//2

        midpc = self.getPiece((middle_col, middle_row))

        if not self.isSquareEmpty(newcoord):
            return False 
        
        coldiff, rowdiff = p - i, r - j
        if abs(coldiff) != abs(rowdiff):
            return False 
        
        if not isKing:
            if color == (255, 255, 255): # so if we have a white piece 
                if rowdiff == 1:
                    return True
                elif rowdiff == 2:
                    return (not self.isSquareEmpty((middle_col, middle_row))) and (color != midpc.color)
            else:
                if rowdiff == -1:
                    return True
                elif rowdiff == -2:
                    return (not self.isSquareEmpty((middle_col, middle_row))) and (color != midpc.color)
        else:
            if color == (255, 192, 203): # a red king
                if rowdiff == 1 or rowdiff == -1:
                    return True 
                elif abs(rowdiff) == 2:
                    return (not self.isSquareEmpty((middle_col, middle_row))) and ((255, 255, 255) == midpc.color)
            elif color == (118, 238, 0): # a white king
                if rowdiff == 1 or rowdiff == -1:
                    return True 
                elif abs(rowdiff) == 2:
                    return (not self.isSquareEmpty((middle_col, middle_row))) and ((255, 255, 255) != midpc.color)

        return False
    
    def kingify(self, coord):
        pc = self.getPiece(coord)
        if pc is None:
            return 
        _, j = coord[0], coord[1]
        if (j != 0 and j != 7):
            return 

        
        if pc.color != (255, 255, 255) and j == 0:
            pc.set_color((255, 192, 203))
        elif pc.color == (255, 255, 255) and j == 7:
            pc.set_color((118, 238, 0))
        
        pc.make_king()
        

from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
        ##self.board = [[None for _ in range(size)] for _ in range(size)]

    def _create(self):        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = {6, 7} if color == "white" else {1, 0}

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col].piece = Square(row_pawn, col, Pawn(color))
        
        # knights
        self.squares[row_other][1].piece = Square(row_other, 1, Knight(color))
        self.squares[row_other][6].piece = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2].piece = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5].piece = Square(row_other, 5, Bishop(color)) 

        # rooks
        self.squares[row_other][0].piece = Square(row_other, 0, Rook(color))
        self.squares[row_other][7].piece = Square(row_other, 7, Rook(color))
        
        # queen
        self.squares[row_other][3].piece = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4].piece = Square(row_other, 4, King(color))
from tetriminos import *
from assets import *
import random


class Board(): 
    def __init__(self):
        self.board = [[[0, False] for col in range(WIDTH)] for row in range(HEIGHT)]

        self.has_piece = False
        self.piece = None
        self.tetrimino_types = (Tetrimino_T, Tetrimino_O, Tetrimino_Z, Tetrimino_S, Tetrimino_I, Tetrimino_L, Tetrimino_J)
        self.next_piece = random.choice(self.tetrimino_types)

        self.rows_cleared = []
        self.rows_cleared_number = []
        self.score = 0
        self.level = 1

    def add_tetrimino(self):
        spawn = self.next_piece
        lose = False
        for pos in spawn.orig_pos:
            if self.board[pos[0]][pos[1]] != [0, False]:
                lose = True
        self.piece = spawn(self)
        self.next_piece = self.get_next_tetrimino()
        return not lose
        

    def get_next_tetrimino(self):
        return random.choice(self.tetrimino_types)

    def shift_left(self):
        if any(0 == coord[1] for coord in self.piece.position):
            return
        for coord in self.piece.position:
            if self.board[coord[0]][coord[1] - 1][1] is True:
                return
        for row in range(HEIGHT):
            for col in range(WIDTH - 1):
                if self.board[row][col][1] is False and self.board[row][col + 1][1] is False:
                    self.board[row][col] = self.board[row][col + 1].copy()
                    self.board[row][col + 1] = [0, False]                    
        for coord in self.piece.position:
            coord[1] -= 1

    def shift_right(self):
        if any(WIDTH - 1 == coord[1] for coord in self.piece.position):
            return
        for coord in self.piece.position:
            if self.board[coord[0]][coord[1] + 1][1] is True:
                return       
        for row in range(HEIGHT):
            for col in range(WIDTH - 1, 0, -1):
                if self.board[row][col][1] is False and self.board[row][col - 1][1] is False:
                    self.board[row][col] = self.board[row][col - 1].copy()
                    self.board[row][col - 1] = [0, False]                   
        for coord in self.piece.position:
            coord[1] += 1

    def shift_down(self):
        if self.check_solid():
            return True
        for row in range(HEIGHT - 1, 0, -1):
            for col in range(WIDTH):
                if self.board[row][col][1] is False and self.board[row - 1][col][1] is False:
                    self.board[row][col] = self.board[row - 1][col].copy()
                    self.board[row - 1][col] = [0, False]
        for coord in self.piece.position:
            coord[0] += 1

    def check_solid(self):
        for x in self.piece.position:
            if HEIGHT - 1 == x[0]:
                self.piece.stop_tetrimino(self)
                return True
        for row in range(HEIGHT - 1, 0, -1):
            for col in range(WIDTH):
                if self.board[row][col][1] is True and self.board[row - 1][col][1] is False:
                    if self.board[row - 1][col][0] != 0:
                        self.piece.stop_tetrimino(self)
                        return True
        return False
    
    def clear_lines(self):
        line_cleared = False
        for row in range(HEIGHT):
            if all(col[0] != 0 and col[1] is True for col in self.board[row]):
                self.rows_cleared.append(self.board[row].copy())
                self.rows_cleared_number.append(row)
                for pos in self.piece.position:
                    pos[0] += 1
                line_cleared = True
        if line_cleared:
            return True
        else:
            return False
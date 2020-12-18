from settings import*

HEIGHT = 24
WIDTH = 10

def can_rotate(board, o_pos, n_pos):
    for i in range(4):
        if n_pos[i] in o_pos:
            continue
        elif not (0 <= n_pos[i][1] < WIDTH and 0 <= n_pos[i][0] < HEIGHT):
            return False
        elif board[n_pos[i][0]][n_pos[i][1]] != [0, False]:
            return False
    return True

def set_block(board, old_pos, position, colour):
    for i in range(4):
        board[old_pos[i][0]][old_pos[i][1]] = [0, False]
    for i in range(4):
        board[position[i][0]][position[i][1]] = [colour, False]

class Tetrimino_T():
    orig_pos = [[4,3], [4,4], [4,5], [5,4]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[4,3], [4,4], [4,5], [5,4]]
        
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0]= 1

    def stop_tetrimino(self, board):
        
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 4 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 4 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        elif self.orientation % 4 == 2:
            self.orientation += 1 if self.orientation_2(board, True) else 0
        elif self.orientation % 4 == 3:
            self.orientation += 1 if self.orientation_3(board, True) else 0
        return True if orig_orientation != self.orientation else False

    def orientation_0(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] + 1, self.position[0][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 1)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[2] = [self.position[2][0] - 1, self.position[2][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 1)
        return True
    
    def orientation_2(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] - 1, self.position[0][1] + 1]
            self.position[2] = [self.position[2][0] + 1, self.position[2][1] + 1]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 1)
        return True
    
    def orientation_3(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[3] = [self.position[3][0] + 1, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 1)
        return True
            

class Tetrimino_O():
    orig_pos = [[5,4], [4,4], [5,5], [4,5]]
    def __init__(self, board):
        board.has_piece = True
        self.position = [[5,4], [4,4], [5,5], [4,5]]
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0]= 2

    def stop_tetrimino(self, board):
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        return True

class Tetrimino_Z():
    orig_pos = [[4,3], [4,4], [5,4], [5,5]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[4,3], [4,4], [5,4], [5,5]]        
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0] = 3

    def stop_tetrimino(self, board):
        
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 2 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 2 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        return True if orig_orientation != self.orientation else False
    def orientation_0(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] + 1, self.position[0][1] - 2]
            self.position[3] = [self.position[3][0] + 1, self.position[3][1]]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 3)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] - 1, self.position[0][1] + 2]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1]]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 3)
        return True

class Tetrimino_S():
    orig_pos = [[4,5], [4,4], [5,4], [5,3]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[4,5], [4,4], [5,4], [5,3]]
        
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0]= 4

    def stop_tetrimino(self, board):
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 2 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 2 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        return True if orig_orientation != self.orientation else False
    def orientation_0(self, board, clockwise):          
        old_pos = self.position.copy()
        if clockwise:
            self.position[2] = [self.position[2][0], self.position[2][1] - 1]
            self.position[3] = [self.position[3][0] + 2, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 4)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[2] = [self.position[2][0], self.position[2][1] + 1]
            self.position[3] = [self.position[3][0] - 2, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 4)
        return True

class Tetrimino_I():
    orig_pos = [[4,3], [4,4], [4,5], [4,6]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[4,3], [4,4], [4,5], [4,6]]
        
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0]= 5

    def stop_tetrimino(self, board):
        
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 2 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 2 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        return True if orig_orientation != self.orientation else False
    def orientation_0(self, board, clockwise):          
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] + 1, self.position[0][1] - 1]
            self.position[2] = [self.position[2][0] - 1, self.position[2][1] + 1]
            self.position[3] = [self.position[3][0] - 2, self.position[3][1] + 2]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 5)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] - 1, self.position[0][1] + 1]
            self.position[2] = [self.position[2][0] + 1, self.position[2][1] - 1]
            self.position[3] = [self.position[3][0] + 2, self.position[3][1] - 2]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 5)
        return True

class Tetrimino_L():
    orig_pos = [[5,3], [4,3], [4,4], [4,5]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[5,3], [4,3], [4,4], [4,5]]
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0] = 6

    def stop_tetrimino(self, board):
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 4 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 4 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        elif self.orientation % 4 == 2:
            self.orientation += 1 if self.orientation_2(board, True) else 0
        elif self.orientation % 4 == 3:
            self.orientation += 1 if self.orientation_3(board, True) else 0
        return True if orig_orientation != self.orientation else False

    def orientation_0(self, board, clockwise):          
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0], self.position[0][1] - 2]
            self.position[1] = [self.position[1][0] - 1, self.position[1][1] - 1]
            self.position[3] = [self.position[3][0] + 1, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 6)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] - 2, self.position[0][1]]
            self.position[1] = [self.position[1][0] - 1, self.position[1][1] + 1]
            self.position[3] = [self.position[3][0] + 1, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 6)
        return True
    
    def orientation_2(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0], self.position[0][1] + 2]
            self.position[1] = [self.position[1][0] + 1, self.position[1][1] + 1]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 6)
        return True

    def orientation_3(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] + 2, self.position[0][1]]
            self.position[1] = [self.position[1][0] + 1, self.position[1][1] - 1]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 6)
        return True

class Tetrimino_J():
    orig_pos = [[5,5], [4,5], [4,4], [4,3]]
    def __init__(self, board):
        board.has_piece = True
        self.orientation = 1
        self.position = [[5,5], [4,5], [4,4], [4,3]]
        
        for co_ords in self.position:
            board.board[co_ords[0]][co_ords[1]][0] = 7

    def stop_tetrimino(self, board):
        
        for co_ords in self.position:
           board.board[co_ords[0]][co_ords[1]][1] = True
        board.has_piece = False

    def rotate_ccw(self, board):
        orig_orientation = self.orientation
        if self.orientation % 4 == 0:
            self.orientation += 1 if self.orientation_0(board, True) else 0
        elif self.orientation % 4 == 1:
            self.orientation += 1 if self.orientation_1(board, True) else 0
        elif self.orientation % 4 == 2:
            self.orientation += 1 if self.orientation_2(board, True) else 0
        elif self.orientation % 4 == 3:
            self.orientation += 1 if self.orientation_3(board, True) else 0
        return True if orig_orientation != self.orientation else False
    def orientation_0(self, board, clockwise):          
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] + 2, self.position[0][1]]
            self.position[1] = [self.position[1][0] + 1, self.position[1][1] + 1]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 7)
        return True
    
    def orientation_1(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0], self.position[0][1] - 2]
            self.position[1] = [self.position[1][0] + 1, self.position[1][1] - 1]
            self.position[3] = [self.position[3][0] - 1, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 7)
        return True
    
    def orientation_2(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0] - 2, self.position[0][1]]
            self.position[1] = [self.position[1][0] - 1, self.position[1][1] - 1]
            self.position[3] = [self.position[3][0] + 1, self.position[3][1] + 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 7)
        return True

    def orientation_3(self, board, clockwise):
        old_pos = self.position.copy()
        if clockwise:
            self.position[0] = [self.position[0][0], self.position[0][1] + 2]
            self.position[1] = [self.position[1][0] - 1, self.position[1][1] + 1]
            self.position[3] = [self.position[3][0] + 1, self.position[3][1] - 1]
            if not can_rotate(board, old_pos, self.position):   
                self.position = old_pos
                return False
        set_block(board, old_pos, self.position, 7)
        return True


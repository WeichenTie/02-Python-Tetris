from settings import *
import tetriminos
import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TRANSPARENT = 0
OPAQUE = 255

def draw_text(surface, font_name, text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def draw_board(surface, board, assets):
    row_offset = -BLOCK_DIMENSIONS * 10
    skipped = 0
    drawn_first_row = False
    for row in board.board:
        drawn_first_col = False
        if drawn_first_row is True: row_offset -= 1
        if skipped < 4:
            skipped += 1 
            continue
        col_offset = -BLOCK_DIMENSIONS * 5
        for block in row:
            if drawn_first_col is True: col_offset -= 1
            draw_block(surface, board, col_offset, row_offset, block[0], assets)
            col_offset += BLOCK_DIMENSIONS
            drawn_first_col = True
        row_offset += BLOCK_DIMENSIONS
        drawn_first_row = True

def draw_block(surface, board, col_offset, row_offset, color, assets):
    co_ordinates = (WINDOW_WIDTH/2 + col_offset, WINDOW_HEIGHT/2 + row_offset)
    if color == 0:
        assets.blank_block.rect.topleft = co_ordinates
        surface.blit(assets.blank_block.image, assets.blank_block.rect)
    elif color == 1:
        assets.yellow_block.rect.topleft = co_ordinates
        surface.blit(assets.yellow_block.image, assets.yellow_block.rect)
    elif color == 2:
        assets.red_block.rect.topleft = co_ordinates
        surface.blit(assets.red_block.image, assets.red_block.rect)
    elif color == 3:
        assets.green_block.rect.topleft = co_ordinates
        surface.blit(assets.green_block.image, assets.green_block.rect)
    elif color == 4:
        assets.cyan_block.rect.topleft = co_ordinates
        surface.blit(assets.cyan_block.image, assets.cyan_block.rect)
    elif color == 5:
        assets.orange_block.rect.topleft = co_ordinates
        surface.blit(assets.orange_block.image, assets.orange_block.rect)
    elif color == 6:
        assets.blue_block.rect.topleft = co_ordinates
        surface.blit(assets.blue_block.image, assets.blue_block.rect)
    elif color == 7:
        assets.purple_block.rect.topleft = co_ordinates
        surface.blit(assets.purple_block.image, assets.purple_block.rect)
    elif color == 9:
        assets.debug.rect.topleft = co_ordinates
        surface.blit(assets.debug.image, assets.debug.rect)

def draw_next_tetrimino(surface, board, assets):
    offset = 0
    for piece in [board.queued_piece1, board.queued_piece2, board.queued_piece3, board.queued_piece4]:
        if piece == tetriminos.Tetrimino_T:
            assets.T_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.T_next.image, assets.T_next.rect)
        elif piece == tetriminos.Tetrimino_O:
            assets.O_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.O_next.image, assets.O_next.rect)
        elif piece == tetriminos.Tetrimino_L:
            assets.L_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.L_next.image, assets.L_next.rect)
        elif piece == tetriminos.Tetrimino_J:
            assets.J_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.J_next.image, assets.J_next.rect)
        elif piece == tetriminos.Tetrimino_S:
            assets.S_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.S_next.image, assets.S_next.rect)
        elif piece == tetriminos.Tetrimino_Z:
            assets.Z_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/6 + offset)
            surface.blit(assets.Z_next.image, assets.Z_next.rect)
        elif piece == tetriminos.Tetrimino_I:
            assets.I_next.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 2, WINDOW_HEIGHT/6 + offset + 20)
            surface.blit(assets.I_next.image, assets.I_next.rect)
        offset += 120

def draw_board_border(surface, assets):
    surface.blit(assets.board_border.image, assets.board_border.rect)

def draw_pause_screen(surface, assets):
    surface.blit(assets.pause_screen.image, assets.pause_screen.rect)

def draw_start_screen(surface, assets):
    surface.blit(assets.start_screen.image, assets.start_screen.rect)

def draw_game_over_screen(surface, assets):
    surface.blit(assets.start_screen.image, assets.start_screen.rect)

def draw_held_tetrimino(surface, board, assets):
    if type(board.held_piece) == tetriminos.Tetrimino_T:
        assets.T_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.T_next.image, assets.T_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_O:
        assets.O_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.O_next.image, assets.O_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_L:
        assets.L_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.L_next.image, assets.L_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_J:
        assets.J_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.J_next.image, assets.J_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_S:
        assets.S_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.S_next.image, assets.S_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_Z:
        assets.Z_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 10)
        surface.blit(assets.Z_next.image, assets.Z_next.rect)
    elif type(board.held_piece) == tetriminos.Tetrimino_I:
        assets.I_next.rect.midtop = (WINDOW_WIDTH/3 + 29, WINDOW_HEIGHT/6 + 30)
        surface.blit(assets.I_next.image, assets.I_next.rect)
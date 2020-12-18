import pygame
import draw
import board
import os

import assets

from settings import*


class Game():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    TRANSPARENT = 0
    OPAQUE = 255

    FPS = 300
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"background.png")).convert()
        self.rect = self.image.get_rect()
        
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(160,50)

        self.board = board.Board()
        
        self.assets = assets.AllSprites()
        self.audio = assets.AllAudio()
        pygame.font.init()

        self.game_speed = DEFAULT_SPEED
        self.last_update = pygame.time.get_ticks()
        self.last_shift = pygame.time.get_ticks()
        
        self.running = True
        self.waiting = True
        
        self.start = True
        self.pause = False
        self.game_cont = True

        self.UP_up = True
        self.space_up = True
        self.held_not_used = True
        self.esc_up = True
    
    def event(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    self.board.shift_left()
                elif ev.key == pygame.K_RIGHT:
                    self.board.shift_right()
                elif ev.key == pygame.K_UP and self.UP_up:
                    if self.board.piece.rotate_ccw(self.board.board):
                        self.audio.spin_sound.play()
                    self.UP_up = False
                elif ev.key == pygame.K_DOWN:
                    self.board.shift_down()
                    now = pygame.time.get_ticks()
                    self.last_shift = now
                elif ev.key == pygame.K_q and self.held_not_used:
                    self.board.hold_tetrimino()
                    self.held_not_used = False
                    now = pygame.time.get_ticks()
                    self.last_shift = now
                elif ev.key == pygame.K_SPACE and self.space_up:
                    now = pygame.time.get_ticks()
                    self.last_shift = now
                    self.space_up = False
                    for i in range(24):
                        if self.board.shift_down() is True:
                            break
                    self.audio.hard_drop_sound.play()
                elif ev.key == pygame.K_ESCAPE and self.esc_up:
                    self.audio.pause_sound.play()
                    self.waiting = True
                    self.pause = True
                    self.esc_up = False
                elif ev.key == pygame.K_r:
                    self.board = board.Board()
                    self.waiting = True
                    self.start = True
                    self.waiting_screen()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_UP:
                    self.UP_up = True
                if ev.key == pygame.K_SPACE:
                    self.space_up = True

    def update(self):
        self.game_speed
        now = pygame.time.get_ticks()
        if now - self.last_update > self.game_speed:
            self.last_update = now
            if now - self.last_shift > self.game_speed:
                self.board.shift_down()
                self.last_shift = now
        if self.board.clear_lines():
            self.audio.line_clear_sound.play()
            self.blinking_lines()
        if self.board.has_piece is False:
            self.held_not_used = True
            if not self.board.add_tetrimino():
                self.waiting = True
                self.game_cont = False
                pygame.mixer.music.stop()
                self.audio.game_over_sound.play()
                self.last_update = now
        self.board.level = int(self.board.score/10) + 1
        self.game_speed = DEFAULT_SPEED * (84/100)**(self.board.level - 1)
        #self.debug()
    
    def render(self):
        self.screen.fill(self.WHITE)
        self.screen.blit(self.image, self.rect)
        draw.draw_board_border(self.screen, self.assets)
        draw.draw_next_tetrimino(self.screen, self.board, self.assets)
        draw.draw_held_tetrimino(self.screen, self.board, self.assets)
        draw.draw_board(self.screen, self.board, self.assets)
        draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(int(self.clock.get_fps())), 30, self.YELLOW, 30, WINDOW_HEIGHT - 40)
        draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(self.board.score), 70, self.BLACK, WINDOW_WIDTH - WINDOW_WIDTH/3 - 40, WINDOW_HEIGHT - WINDOW_HEIGHT/3)
        pygame.display.flip()
    
    def waiting_screen(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running = False
                self.waiting = False
            if ev.type == pygame.KEYDOWN:
                if ev.key != pygame.K_ESCAPE:
                    self.waiting = False
                    self.start = False
                    if not self.pause:
                        pygame.mixer.music.play(-1)
                    self.pause = False
                    self.space_up = False
                    self.esc_up = True

                

        self.screen.fill(self.WHITE)
        self.screen.blit(self.image, self.rect)
        draw.draw_board_border(self.screen, self.assets)
        draw.draw_board(self.screen, self.board, self.assets)
        draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(int(self.clock.get_fps())), 30, self.YELLOW, 30, WINDOW_HEIGHT - 40)
        draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(self.board.score), 70, self.BLACK, WINDOW_WIDTH - WINDOW_WIDTH/3 - 40, WINDOW_HEIGHT - WINDOW_HEIGHT/3)
        draw.draw_next_tetrimino(self.screen, self.board, self.assets)
        draw.draw_held_tetrimino(self.screen, self.board, self.assets)
        if self.start:
            draw.draw_start_screen(self.screen, self.assets)
        elif self.pause:
            draw.draw_pause_screen(self.screen, self.assets)
        elif not self.game_cont:
            draw.draw_game_over_screen(self.screen, self.assets)
        pygame.display.flip()
        

    def blinking_lines(self):
        blinks = 0
        orig_lines = self.board.rows_cleared.copy()
        while blinks < 6:
            self.clock.tick(self.FPS)            
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    self.waiting = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.waiting = True
                        self.esc_up = False

            now = pygame.time.get_ticks()
            if now - self.last_update > 75:
                self.last_update = now
                
                for i in range(len(orig_lines)):
                    if blinks % 2 == 0:
                        self.board.board[self.board.rows_cleared_number[i]] = [[0, False] for j in range(WIDTH)]
                    else:
                        self.board.board[self.board.rows_cleared_number[i]] = orig_lines[i]
                blinks += 1
            self.screen.fill(self.WHITE)
            self.screen.blit(self.image, self.rect)
            draw.draw_board_border(self.screen, self.assets)
            draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(int(self.clock.get_fps())), 30, self.YELLOW, 30, WINDOW_HEIGHT - 40)
            draw.draw_text(self.screen, pygame.font.match_font('Vermin Vibes 2 Soft'), str(self.board.score), 70, self.BLACK, WINDOW_WIDTH - WINDOW_WIDTH/3 - 40, WINDOW_HEIGHT - WINDOW_HEIGHT/3)
            draw.draw_board(self.screen, self.board, self.assets)
            draw.draw_next_tetrimino(self.screen, self.board, self.assets)
            draw.draw_held_tetrimino(self.screen, self.board, self.assets)
            pygame.display.flip()
            
        for row in self.board.rows_cleared_number:
            self.board.score += 1
            del self.board.board[row]
            self.board.board.insert(0, [[0, False] for i in range(WIDTH)])
        self.board.rows_cleared_number.clear()
        self.board.rows_cleared.clear()
        self.space_up = True
    

    def debug(self):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if self.board.board[i][j][1] is True and self.board.board[i][j][0] != 9:
                    self.board.board[i][j] = [9, True]
                    #print(self.board.board[i][j])
        
        for i in self.board.piece.position:
            self.board.board[i[0]][i[1]] = [9, False]
        #print("done")

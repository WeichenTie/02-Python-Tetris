"""
Code written by Weichen Tie
Art created by James Wu
"""


from game import Game
from board import Board
import pygame



game = Game()
while game.running:
    game.clock.tick(game.FPS)
    while game.waiting is True:
        game.clock.tick(game.FPS)
        game.waiting_screen()
        game.last_update = pygame.time.get_ticks()
        game.last_update = pygame.time.get_ticks()
        game.space_up = True
    if not game.running:
        break
    if not game.game_cont:
        game.board = Board()
        game.game_cont = True
    game.event()
    if not game.waiting:
        game.update()
        game.render()
pygame.quit()
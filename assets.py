import pygame
from settings import *

class BlankBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"blank.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class OrangeBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"orange.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class BlueBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"blue.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class RedBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"red.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class YellowBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"yellow.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class CyanBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"cyan.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class PurpleBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"purple.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class GreenBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"green.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()

class DebugBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"debug.png")).convert()
        self.image = pygame.transform.scale(self.image, BLOCK_SIZE)
        self.rect = self.image.get_rect()


class TNext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"T_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

class ONext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"O_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
class INext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"I_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 2, WINDOW_HEIGHT/5)
class ZNext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"Z_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/5)
class SNext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"S_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/5)
class LNext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"L_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/5)
class JNext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"J_BLOCK.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midtop = (WINDOW_WIDTH - WINDOW_WIDTH/2.82 - 1, WINDOW_HEIGHT/5)

class BoardBorder(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"border.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((WINDOW_WIDTH/2 - 10, WINDOW_HEIGHT/2 - 10))

class PauseScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"PauseScreen.png")).convert()
        self.image.set_alpha(180)
        self.rect = self.image.get_rect()
        self.rect.center = ((WINDOW_WIDTH/2 - 5, WINDOW_HEIGHT/2 - 10))

class StartScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER,"StartScreen.png")).convert()
        self.image.set_alpha(180)
        self.rect = self.image.get_rect()
        self.rect.center = ((WINDOW_WIDTH/2 - 5, WINDOW_HEIGHT/2 - 10))

class AllSprites():
    def __init__(self):
        self.blank_block = BlankBlock()
        self.blue_block = BlueBlock()
        self.orange_block = OrangeBlock()
        self.red_block = RedBlock()
        self.yellow_block = YellowBlock()
        self.cyan_block = CyanBlock()
        self.purple_block = PurpleBlock()
        self.green_block = GreenBlock()
        self.debug = DebugBlock()

        self.T_next = TNext()
        self.O_next = ONext()
        self.I_next = INext()
        self.S_next = SNext()
        self.Z_next = ZNext()
        self.L_next = LNext()
        self.J_next = JNext()

        self.board_border = BoardBorder()
        self.pause_screen = PauseScreen()
        self.start_screen = StartScreen()

class AllAudio():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(THEME)
        pygame.mixer.music.set_volume(0.1)

        self.spin_sound = pygame.mixer.Sound(os.path.join(AUDIO_FOLDER,"spin.ogg"))
        self.spin_sound.set_volume(0.15)
        
        self.line_clear_sound = pygame.mixer.Sound(os.path.join(AUDIO_FOLDER,"clear.ogg"))
        self.line_clear_sound.set_volume(0.3)

        self.pause_sound = pygame.mixer.Sound(os.path.join(AUDIO_FOLDER,"pause.ogg"))
        self.pause_sound.set_volume(0.15)

        self.game_over_sound = pygame.mixer.Sound(os.path.join(AUDIO_FOLDER,"gameover.ogg"))
        self.game_over_sound.set_volume(0.15)

        self.hard_drop_sound = pygame.mixer.Sound(os.path.join(AUDIO_FOLDER,"harddrop.ogg"))
        self.hard_drop_sound.set_volume(0.15)
        
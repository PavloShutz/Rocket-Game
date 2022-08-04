import pygame as pg
from pygame.sprite import Sprite
from pygame.mixer import Sound


class Bullet(Sprite):

    def __init__(self, rocket_game):
        super().__init__()
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.color = self.settings.bullet_color
        self.laser_sound = Sound('laser-sound-effect-1-11002.mp3')

        self.rect = pg.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
        self.rect.midtop = rocket_game.rocket.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)

    def create_laser_sound(self):
        pg.mixer.Sound.play(self.laser_sound, maxtime=90)

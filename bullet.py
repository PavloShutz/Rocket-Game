import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, rocket_game):
        super().__init__()
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.color = self.settings.bullet_color

        self.rect = pg.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
        self.rect.midtop = rocket_game.rocket.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)

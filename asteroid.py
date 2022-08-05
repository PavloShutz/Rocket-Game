import pygame
from pygame.sprite import Sprite
from random import randint


class Asteroid(Sprite):
    """Representing asteroid in space"""
    def __init__(self, rocket_game):
        super().__init__()
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings

        self.image = pygame.image.load('asteroid.png')
        self.rect = self.image.get_rect()

        self.rect.x = randint(
            0, self.settings.screen_width - 10
        )
        self.rect.y = randint(self.rect.height,
                              self.rect.height + 20)

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.asteroid_speed
        self.rect.y = self.y

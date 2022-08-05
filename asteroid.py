from random import randint, choice

import pygame
from pygame.sprite import Sprite
from pygame.mixer import Sound


class Asteroid(Sprite):
    """Representing asteroid in space"""
    def __init__(self, rocket_game):
        super().__init__()
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings

        self.image = pygame.image.load(choice(self.settings.asteroid_images))
        self.rect = self.image.get_rect()
        self.explosion = Sound("explosion.wav")

        self.rect.x = randint(
            0, self.settings.screen_width - 10
        )
        self.rect.y = randint(self.rect.height + 30,
                              self.rect.height + 90)

        self.y = float(self.rect.y)

    def __del__(self):
        pygame.mixer.Sound.play(self.explosion)

    def update(self):
        self.y += self.settings.asteroid_speed
        self.rect.y = self.y

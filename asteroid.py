import pygame
from pygame.sprite import Sprite


class Asteroid(Sprite):
    """Representing asteroid in space"""
    def __init__(self, rocket_game):
        super().__init__()
        self.screen = rocket_game.screen

        self.image = pygame.image.load('asteroid.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

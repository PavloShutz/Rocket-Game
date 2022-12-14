import pygame
from pygame.mixer import Sound


class Settings:
    """Class for all game settings"""

    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (232, 255, 245)

        self.rocket_speed = 0.5

        self.bullet_speed = 0.75
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        self.asteroid_speed = 0.1
        self.asteroid_images = ['asteroid1.png', 'asteroid2.png']
        self.explosion = Sound("explosion.wav")
        self.game_over_sound = Sound("game_over.wav")

        self.text = \
            "Press \"Space\" to restart game or Press \"q\" to quit current game."
        self.font = pygame.font.Font(r"C:\Windows\Fonts\arial.ttf", 35)
        self.restart_text = self.font.render(self.text, True, (0, 255, 0))
        self.text_position = self.restart_text.get_rect()
        self.text_position.center = (
            self.screen_width // 2,
            self.screen_height // 2,
        )

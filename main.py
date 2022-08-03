import sys

import pygame

from settings import Settings
from rocket import Rocket


class RocketGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Rocket")
        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_updates()
            self.rocket.update()
            self._update_screen()

    def _check_updates(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        elif event.key == pygame.K_UP:
            self.rocket.move_top = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_top = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blit_me()
        pygame.display.flip()


if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()

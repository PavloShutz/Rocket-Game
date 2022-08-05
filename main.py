import sys
from random import randint

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from asteroid import Asteroid


class RocketGame:
    """The main class for Rocket Game"""

    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption("Rocket")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self._create_asteroids()

    def run_game(self):
        while True:
            self._check_updates()
            self.rocket.update()
            self._update_bullets()
            self._update_asteroids()
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
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_top = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            new_bullet.create_laser_sound()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_to_destroy_asteroid()

    def _update_asteroids(self):
        self.asteroids.update()

    def _check_to_destroy_asteroid(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.asteroids, True, True
        )
        # pygame.mixer.Sound.play()

    def _create_asteroids(self):
        asteroid = Asteroid(self)
        asteroid_width = asteroid.rect.width
        available_space_x = self.settings.screen_width - (2 * asteroid_width)
        number_asteroids_x = available_space_x // (2 * asteroid_width)

        for asteroid_number in range(randint(1, number_asteroids_x)):
            asteroid = Asteroid(self)
            asteroid.x = asteroid_width + 2 * asteroid_width * asteroid_number
            asteroid.rect.x = asteroid.x
            self.asteroids.add(asteroid)
        self.asteroids.add(asteroid)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blit_me()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.asteroids.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    rg = RocketGame()
    rg.run_game()

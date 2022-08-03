import pygame


class Rocket:

    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()

        # centering our rocket
        self.rect.center = self.screen_rect.center

        # setting coordinates for our rocket
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # initializing rocket statement
        self.move_right, self.move_left = False, False
        self.move_top, self.move_down = False, False

    def update(self):
        self._move_rocket_horizontally()
        self._move_rocket_vertically()

        self._update_coordinates()

    def _move_rocket_horizontally(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

    def _move_rocket_vertically(self):
        if self.move_top and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

    def _update_coordinates(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

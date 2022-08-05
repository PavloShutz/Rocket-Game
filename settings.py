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

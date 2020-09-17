import arcade
import logging as log

SCREEN_HEIGHT = 600


class Enemy(arcade.Sprite):

    def __init__(self, *args, speed=2, **kwargs):
        super().__init__(":resources:images/enemies/fly.png", *args, **kwargs)

        self.speed = speed

        self.boundary_top = SCREEN_HEIGHT - 35
        self.boundary_bottom = (SCREEN_HEIGHT / 2) - 30

        self.change_y = self.speed

    def move(self):
        if self.top > self.boundary_top:
            self.change_y = -self.speed
        elif self.bottom < self.boundary_bottom:
            self.change_y = self.speed
        log.debug(f"enemy's center_y is {self.center_y} and its center_x is {self.center_x}")

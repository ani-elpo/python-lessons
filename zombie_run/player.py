import arcade

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600


class Player(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png", *args, **kwargs)

    def move(self):
        self.change_x = 0
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        if self.center_x >= 50:
            arcade.set_viewport(self.center_x - 45, SCREEN_WIDTH + (self.center_x - 45), 0, SCREEN_HEIGHT)

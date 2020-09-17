import arcade

from zombie_run.settings import SCREEN_WIDTH, SCREEN_HEIGHT

MOVEMENT_SPEED = 4
JUMP_SPEED = 23


class Player(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png", *args, **kwargs)
        self.left_pressed = False
        self.right_pressed = False
        self.jump_pressed = False

    def move(self, can_jump=False):
        self.change_x = 0
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        if self.center_x >= 50:
            arcade.set_viewport(self.center_x - 45, SCREEN_WIDTH + (self.center_x - 45), 0, SCREEN_HEIGHT)

        if self.left_pressed and not self.right_pressed:
            self.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = MOVEMENT_SPEED
        if self.jump_pressed:
            if can_jump:
                self.change_y = JUMP_SPEED
                self.jump_pressed = False

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.jump_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        if key == arcade.key.W:
            self.jump_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.jump_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        if key == arcade.key.W:
            self.jump_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False

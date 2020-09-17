import logging as log
import arcade

from zombie_run.level import Level

log.basicConfig(format='%(asctime)s  %(levelname)8s:  %(message)s', level=log.INFO)

from zombie_run.enemy import Enemy
from zombie_run.player import Player

SPIKES_ACTIVE = False

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600
SCREEN_TITLE = "zombie game"

TILE_SCALE = 0.5
TILE_SIZE = 64

COLLECT_SCALE = 1 / 4.25

BOX_NO = 5
PLAT_NO = 5

MOVEMENT_SPEED = 4

GRAVITY = 2
JUMP_SPEED = 23


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.level = None

        self.left_pressed = False
        self.right_pressed = False
        self.jump_pressed = False

        self.physics_engine = None

        self.zombie = None

        self.score = None

        self.game_over = False

    def setup(self):
        self.level = Level()

        self.level.setup_map()

        self.setup_zombie()

        self.score = 0

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite=self.zombie,
                                                             platforms=self.level.obstacle_list,
                                                             gravity_constant=GRAVITY)

    def setup_zombie(self):
        self.zombie = Player(scale=TILE_SCALE, center_x=TILE_SIZE / 2, center_y=TILE_SIZE + TILE_SIZE / 2)

    def on_draw(self):
        arcade.start_render()

        self.level.draw_background()
        self.zombie.draw()
        self.level.draw_foreground()

        output = f"Score: {self.score}"
        arcade.draw_text(output, self.zombie.center_x - 35, self.zombie.center_y + 20, arcade.color.WHITE, 20)

    def on_update(self, delta_time):

        self.zombie.move()

        if self.left_pressed and not self.right_pressed:
            self.zombie.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.zombie.change_x = MOVEMENT_SPEED
        if self.jump_pressed:
            if self.physics_engine.can_jump():
                self.zombie.change_y = JUMP_SPEED
                self.jump_pressed = False

        hit_list = arcade.check_for_collision_with_list(self.zombie,
                                                        self.level.collectibles)

        for item in hit_list:
            self.level.collectibles.remove(item)
            self.score += 1

        for enemy in self.level.enemies:
            enemy.move()

        self.level.enemies.update()

        if len(arcade.check_for_collision_with_list(self.zombie, self.level.enemies)) > 0:
            self.game_over = True
            log.info(f"game over")

        if len(arcade.check_for_collision_with_list(self.zombie, self.level.spikes)) > 0 and SPIKES_ACTIVE:
            self.game_over = True

        if self.game_over:
            self.score = 0
            self.setup()
            self.game_over = False
            log.info(f"game restarting")

        self.physics_engine.update()

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


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

# homework: refactor all code (unused code + comments, naming, single responsibility)

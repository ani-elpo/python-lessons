import logging as log
import arcade

from zombie_run.level import Level
from zombie_run.player import Player
from zombie_run.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, TILE_SIZE, TILE_SCALE

log.basicConfig(format='%(asctime)s  %(levelname)8s:  %(message)s', level=log.INFO)

SPIKES_ACTIVE = False


GRAVITY = 2


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.level = None

        self.physics_engine = None

        self.zombie = None

        self.score = None

        self.game_over = False

    def setup(self):
        self.level = Level(level=2)

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

        self.zombie.move(can_jump=self.physics_engine.can_jump())

        self.check_collectibles()

        self.update_enemies()

        self.check_for_game_over()

        if self.game_over:
            self.restart_game()

        self.physics_engine.update()

    def restart_game(self):
        self.score = 0
        self.setup()
        self.game_over = False
        log.info(f"game restarting")

    def check_for_game_over(self):
        if len(arcade.check_for_collision_with_list(self.zombie, self.level.enemies)) > 0:
            self.game_over = True
            log.info(f"game over")
        if len(arcade.check_for_collision_with_list(self.zombie, self.level.spikes)) > 0 and SPIKES_ACTIVE:
            self.game_over = True

    def update_enemies(self):
        for enemy in self.level.enemies:
            enemy.move()
        self.level.enemies.update()

    def check_collectibles(self):
        hit_list = arcade.check_for_collision_with_list(self.zombie,
                                                        self.level.collectibles)
        for item in hit_list:
            self.level.collectibles.remove(item)
            self.score += 1

    def on_key_press(self, key, modifiers):
        self.zombie.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.zombie.on_key_release(key, modifiers)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

# homework: refactor all code (unused code + comments, naming, single responsibility)

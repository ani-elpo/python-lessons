import logging as log
import arcade

log.basicConfig(format='%(asctime)s  %(levelname)8s:  %(message)s', level=log.INFO)

from zombie_run.enemy import Enemy

SPIKES_ACTIVE = False

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600
SCREEN_TITLE = "zombie game"

TILE_SCALE = 0.5
TILE_SIZE = 64

COLLECT_SCALE = 1/4.25

BOX_NO = 5
PLAT_NO = 5

MOVEMENT_SPEED = 4

GRAVITY = 2
JUMP_SPEED = 23




class Player(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png", *args, **kwargs)

    def move(self):
        self.change_x = 0
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        if self.center_x >= 50:
            arcade.set_viewport(self.center_x - 45, SCREEN_WIDTH + (self.center_x - 45), 0, SCREEN_HEIGHT)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.left_pressed = False
        self.right_pressed = False
        self.jump_pressed = False

        self.physics_engine = None

        self.zombie = None
        self.ground = None
        self.boxes = None
        self.plats = None
        self.water = None
        self.obstacle_list = None
        self.enemies = None
        self.spikes = None

        self.collectibles = None

        self.score = None

        self.game_over = False

    def setup(self):
        self.obstacle_list = arcade.SpriteList()

        self.setup_zombie()
        self.setup_map()

        self.score = 0

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite=self.zombie,
                                                             platforms=self.obstacle_list,
                                                             gravity_constant=GRAVITY)


    def setup_zombie(self):
        self.zombie = Player(scale=TILE_SCALE, center_x=TILE_SIZE / 2, center_y=TILE_SIZE + TILE_SIZE / 2)

    def setup_map(self):
        map_name = "maps/level1.tmx"
        log.info(f"map loaded")
        ground_layer_name = 'ground layer'
        collectible_layer_name = 'collectible layer'

        water_layer_name = 'water layer'

        platform_layer_name = 'platform layer'

        box_layer_name = 'box layer'

        spike_layer_name = 'spike layer'

        enemies_layer_name = 'enemies layer'

        my_map = arcade.tilemap.read_tmx(map_name)

        self.ground = arcade.tilemap.process_layer(map_object=my_map,
                                                   layer_name=ground_layer_name,
                                                   scaling=TILE_SCALE)
        self.collectibles = arcade.tilemap.process_layer(map_object=my_map,
                                                   layer_name=collectible_layer_name,
                                                   scaling=TILE_SCALE)
        self.water = arcade.tilemap.process_layer(map_object=my_map, layer_name=water_layer_name, scaling=TILE_SCALE)
        self.plats = arcade.tilemap.process_layer(map_object=my_map, layer_name=platform_layer_name, scaling=TILE_SCALE)
        self.boxes = arcade.tilemap.process_layer(map_object=my_map, layer_name=box_layer_name, scaling=TILE_SCALE)
        self.spikes = arcade.tilemap.process_layer(map_object=my_map, layer_name=spike_layer_name, scaling=TILE_SCALE)

        enemies = arcade.tilemap.process_layer(map_object=my_map, layer_name=enemies_layer_name, scaling=TILE_SCALE)
        self.enemies = arcade.SpriteList()

        def translate_tiled_y_coords(map_height, tiled_coord):
            new_coord = map_height * TILE_SIZE - tiled_coord * TILE_SCALE
            return new_coord

        for sprite in enemies:
            fly = Enemy(center_x=sprite.center_x, center_y=sprite.center_y, scale=sprite.scale)
            fly.texture = sprite.texture

            fly.boundary_top = translate_tiled_y_coords(my_map.map_size.height, sprite.properties["max_y"])
            fly.boundary_bottom = translate_tiled_y_coords(my_map.map_size.height, sprite.properties["min_y"])

            self.enemies.append(fly)

        self.obstacle_list.extend(self.ground)
        self.obstacle_list.extend(self.plats)
        self.obstacle_list.extend(self.boxes)

    def on_draw(self):

        arcade.start_render()
        self.water.draw()
        self.ground.draw()
        self.plats.draw()
        self.zombie.draw()
        self.boxes.draw()
        self.collectibles.draw()
        self.spikes.draw()
        self.enemies.draw()

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
                                                        self.collectibles)

        for item in hit_list:
            self.collectibles.remove(item)
            self.score += 1

        for enemy in self.enemies:
            enemy.move()

        self.enemies.update()

        if len(arcade.check_for_collision_with_list(self.zombie, self.enemies)) > 0:
            self.game_over = True
            log.info(f"game over")

        if len(arcade.check_for_collision_with_list(self.zombie, self.spikes)) > 0 and SPIKES_ACTIVE:
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



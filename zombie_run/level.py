import logging as log

import arcade

from zombie_run.enemy import Enemy
from zombie_run.settings import TILE_SCALE, TILE_SIZE


class Level:
    def __init__(self):
        self.ground = None
        self.boxes = None
        self.plats = None
        self.water = None
        self.obstacle_list = None
        self.enemies = None
        self.spikes = None
        self.collectibles = None

    def setup_map(self):
        self.obstacle_list = arcade.SpriteList()

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

    def draw_background(self):
        self.ground.draw()
        self.plats.draw()
        self.boxes.draw()
        self.collectibles.draw()
        self.spikes.draw()
        self.enemies.draw()

    def draw_foreground(self):
        self.water.draw()

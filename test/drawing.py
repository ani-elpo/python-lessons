import math

import arcade

# Set constants for the screen size
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600
SCREEN_TITLE = "zombie game"

TILE_SCALE = 0.5
TILE_SIZE = 64

COLLECT_SCALE = 1/4.25

BOX_NO = 5
PLAT_NO = 5

MOVEMENT_SPEED = 4

GRAVITY = 1
JUMP_SPEED = 18


class Enemy(arcade.Sprite):

    def __init__(self, *args, speed=2, **kwargs):
        super().__init__(":resources:images/enemies/fly.png", *args, **kwargs)

        self.speed = speed

        self.boundary_top = SCREEN_HEIGHT - 35
        self.boundary_bottom = (SCREEN_HEIGHT/2) - 30


    def move(self):
        if self.top > self.boundary_top:
            self.change_y -= self.speed
        elif self.bottom < self.boundary_bottom:
            self.change_y += self.speed

class Player(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png", *args, **kwargs)

    def move(self):
        self.change_x = 0
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        # for i in range(SCREEN_WIDTH*2):
        if self.center_x >= 50:
            arcade.set_viewport(self.center_x - 45, SCREEN_WIDTH + (self.center_x - 45), 0, SCREEN_HEIGHT)

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.left_pressed = False
        self.right_pressed = False
        self.jump_pressed = False

        self.physics_engine = None

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.zombie = None
        self.ground = None
        self.boxes = None
        self.plats = None
        self.obstacle_list = None
        self.enemies = None

        self.collectibles = None

        self.score = None

        self.game_over = False

    def setup(self):
        # Create your sprites and sprite lists here
        self.obstacle_list = arcade.SpriteList()

        self.setup_zombie()
        self.setup_ground()
        self.setup_boxes()
        self.setup_plats()
        self.setup_collectible()
        self.setup_enemies()

        self.score = 0

        self.physics_engine = arcade.PhysicsEnginePlatformer(player_sprite=self.zombie,
                                                             platforms=self.obstacle_list,
                                                             gravity_constant=GRAVITY)


    def setup_zombie(self):
        self.zombie = Player(scale=TILE_SCALE, center_x=TILE_SIZE / 2, center_y=TILE_SIZE + TILE_SIZE / 2)

    def setup_ground(self):
        self.ground = arcade.SpriteList()

        for i in range(math.ceil(SCREEN_WIDTH / TILE_SIZE)):
                lava = arcade.Sprite(":resources:images/tiles/lava.png", scale=TILE_SCALE, center_x=TILE_SIZE / 2, center_y=TILE_SIZE / 2)
                lava.center_x += i*TILE_SIZE
                self.ground.append(lava)
                self.obstacle_list.append(lava)

    def setup_boxes(self):
        self.boxes = arcade.SpriteList()

        for i in range(BOX_NO):
            box = arcade.Sprite(":resources:images/tiles/boxCrate.png", scale=TILE_SCALE, center_x=TILE_SIZE * 2.5, center_y=TILE_SIZE * 1.5)
            box.center_x += i*(TILE_SIZE+(BOX_NO*40))
            self.boxes.append(box)
            self.obstacle_list.append(box)

    def setup_plats(self):
        self.plats = arcade.SpriteList()

        for i in range(PLAT_NO):
            plat = arcade.Sprite(":resources:images/tiles/dirtHalf_left.png", scale=TILE_SCALE, center_x=TILE_SIZE * 3.5, center_y=TILE_SIZE * 3)
            plat.center_x += i*(TILE_SIZE+(PLAT_NO*40))
            self.plats.append(plat)
            self.obstacle_list.append(plat)

            plat = arcade.Sprite(":resources:images/tiles/dirtHalf_right.png", scale=TILE_SCALE, center_x=(TILE_SIZE * 3.5) + TILE_SIZE, center_y=TILE_SIZE * 3)
            plat.center_x += i*(TILE_SIZE+(PLAT_NO*40))
            self.plats.append(plat)
            self.obstacle_list.append(plat)

    def setup_collectible(self):
        self.collectibles = arcade.SpriteList()

        for i in range(6):
            flask = arcade.Sprite("assets/Colored/genericItem_color_105.png", center_x=TILE_SIZE * 3.5, center_y=(TILE_SIZE * 3)+TILE_SIZE)
            flask.scale = TILE_SIZE/(2*flask.height)
            flask.center_x += i*TILE_SIZE*4
            self.collectibles.append(flask)

    def setup_enemies(self):
        self.enemies = arcade.SpriteList()

        for i in range(3):
            fly = Enemy(speed=1, center_x=SCREEN_WIDTH/2, center_y=(SCREEN_HEIGHT/2) - 30, scale=TILE_SCALE)
            fly.center_x += i*TILE_SIZE*6
            self.enemies.append(fly)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.zombie.draw()
        self.ground.draw()
        self.boxes.draw()
        self.plats.draw()
        self.collectibles.draw()
        self.enemies.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, (SCREEN_WIDTH*1.5)-10, SCREEN_HEIGHT/2, arcade.color.WHITE, 40)




    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        # Calculate speed based on the keys pressed

        self.zombie.move()

        # if self.jump_pressed and not self.down_pressed:
        #     self.zombie.change_y = MOVEMENT_SPEED
        # if self.down_pressed and not self.up_pressed:
        #     self.zombie.change_y = -MOVEMENT_SPEED
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

        if self.game_over:
            self.score = 0
            self.setup()

        # Call update to move the sprite
        # If using a physics engine, call update on it instead of the sprite
        # list.

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

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
        """Called when the user releases a key. """

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
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()



# homework: make the fly go up and down properly DONE
# make more flies DONE
# make player die if it hits fly (restart game)
# put the player in its own class DONE

# (tiled editor) -> download + draw a level
# platformer redux pack from kenney.nl\


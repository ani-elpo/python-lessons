import math

import arcade

# Set constants for the screen size
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 600
SCREEN_TITLE = "zombie game"

TILE_SCALE = 0.25
TILE_SIZE = 32

BOX_NO = 10


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

        # If you have sprite lists, you should create them here,
        # and set them to None

        self.zombie = None
        self.ground = None
        self.boxes = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.setup_zombie()
        self.setup_ground()
        self.setup_boxes()

    def setup_zombie(self):
        self.zombie = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", scale=TILE_SCALE)
        self.zombie.center_x = TILE_SIZE / 2
        self.zombie.center_y = TILE_SIZE + TILE_SIZE / 2
        self.zombie.draw()

    def setup_ground(self):
        self.ground = arcade.SpriteList()

        for i in range(math.ceil(SCREEN_WIDTH / TILE_SIZE)):
                lava = arcade.Sprite(":resources:images/tiles/lava.png", scale=TILE_SCALE, center_x=TILE_SIZE / 2, center_y=TILE_SIZE / 2)
                lava.center_x += i*TILE_SIZE
                self.ground.append(lava)
        self.ground.draw()

    def setup_boxes(self):
        self.boxes = arcade.SpriteList()

        for i in range(BOX_NO):
                box = arcade.Sprite(":resources:images/tiles/boxCrate.png", scale=TILE_SCALE, center_x=TILE_SIZE * 2.5, center_y=TILE_SIZE * 1.5)
                box.center_x += i*(TILE_SIZE+(BOX_NO*7))
                self.boxes.append(box)
        self.boxes.draw()



    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # self.zombie.draw()
        # self.ground.draw()
        # self.boxes.draw()
        self.setup_zombie()
        self.setup_ground()
        self.setup_boxes()




    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """




def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()






# change screen width DONE
# scale zombie and put him on the grass DONE
# place boxes on grass DONE
# create floating platforms
# organise setup method (refactoring)

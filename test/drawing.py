import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "villager"


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.offset = None
        self.offset2 = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.offset = -100
        self.offset2 = 500

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # head
        arcade.draw_rectangle_filled(self.offset + 300, 300, 55, 75, arcade.color.CAMEL)
        # mouth
        arcade.draw_rectangle_filled(self.offset + 300, 274, 30, 7, arcade.color.COCONUT)
        # eyebrows
        arcade.draw_rectangle_filled(self.offset + 300, 300, 45, 7, arcade.color.BLACK)
        # eyes
        arcade.draw_rectangle_filled(self.offset + 282, 293, 8, 7, arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.offset + 317, 293, 8, 7, arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.offset + 290, 293, 8, 7, arcade.color.BRIGHT_GREEN)
        arcade.draw_rectangle_filled(self.offset + 309, 293, 8, 7, arcade.color.BRIGHT_GREEN)
        # hat
        arcade.draw_rectangle_filled(self.offset + 300, 337, 80, 3, arcade.color.BANANA_YELLOW)
        arcade.draw_rectangle_filled(self.offset + 300, 347, 50, 20, arcade.color.BANANA_YELLOW)
        # feet
        arcade.draw_rectangle_filled(self.offset + 300, 135, 40, 30, arcade.color.BROWN_NOSE)
        # body
        arcade.draw_rectangle_filled(self.offset + 300, 205, 55, 115, arcade.color.COCONUT)
        # arms
        arcade.draw_rectangle_filled(self.offset + 300, 240, 105, 45, arcade.color.COCONUT)
        # nose
        arcade.draw_rectangle_filled(self.offset + 300, 265, 15, 40, arcade.color.BROWN_NOSE)

        # draw circle

        arcade.draw_circle_filled(self.offset2, 285, 18, arcade.color.ANTIQUE_RUBY)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.offset += 2
        self.offset2 -= 5



def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()






# setup thingy
# another object moving independently
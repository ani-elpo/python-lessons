"""
Drawing an example happy face

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.happy_face
"""

import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "villager"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

offset = -100


# --- Drawing Commands Will Go Here ---


def villager(delta):
    arcade.start_render()
    global offset
    offset += 1
    # head
    arcade.draw_rectangle_filled(offset+300, 300, 55, 75, arcade.color.CAMEL)
    # mouth
    arcade.draw_rectangle_filled(offset+300, 274, 30, 7, arcade.color.COCONUT)
    # eyebrows
    arcade.draw_rectangle_filled(offset+300, 300, 45, 7, arcade.color.BLACK)
    # eyes
    arcade.draw_rectangle_filled(offset+282, 293, 8, 7, arcade.color.WHITE)
    arcade.draw_rectangle_filled(offset+317, 293, 8, 7, arcade.color.WHITE)
    arcade.draw_rectangle_filled(offset+290, 293, 8, 7, arcade.color.BRIGHT_GREEN)
    arcade.draw_rectangle_filled(offset+309, 293, 8, 7, arcade.color.BRIGHT_GREEN)
    # hat
    arcade.draw_rectangle_filled(offset+300, 337, 80, 3, arcade.color.BANANA_YELLOW)
    arcade.draw_rectangle_filled(offset+300, 347, 50, 20, arcade.color.BANANA_YELLOW)
    # feet
    arcade.draw_rectangle_filled(offset+300, 135, 40, 30, arcade.color.BROWN_NOSE)
    # body
    arcade.draw_rectangle_filled(offset+300, 205, 55, 115, arcade.color.COCONUT)
    # arms
    arcade.draw_rectangle_filled(offset+300, 240, 105, 45, arcade.color.COCONUT)
    # nose
    arcade.draw_rectangle_filled(offset+300, 265, 15, 40, arcade.color.BROWN_NOSE)



arcade.schedule(villager, 1/30)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

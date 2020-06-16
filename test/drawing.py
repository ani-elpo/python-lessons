"""
Drawing an example happy face

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.happy_face
"""

import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Happy Face Example"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

# head
arcade.draw_rectangle_filled(300, 300, 55, 75, arcade.color.CAMEL)
# mouth
arcade.draw_rectangle_filled(300, 274, 30, 7, arcade.color.COCONUT)
# nose
arcade.draw_rectangle_filled(300, 265, 15, 40, arcade.color.BROWN_NOSE)
# eyebrows
arcade.draw_rectangle_filled(300, 300, 45, 7, arcade.color.BLACK)
# eyes
arcade.draw_rectangle_filled(282, 293, 8, 7, arcade.color.WHITE)
arcade.draw_rectangle_filled(317, 293, 8, 7, arcade.color.WHITE)
arcade.draw_rectangle_filled(290, 293, 8, 7, arcade.color.BRIGHT_GREEN)
arcade.draw_rectangle_filled(309, 293, 8, 7, arcade.color.BRIGHT_GREEN)
# hat
arcade.draw_rectangle_filled(300, 337, 70, 3, arcade.color.BANANA_YELLOW)


# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

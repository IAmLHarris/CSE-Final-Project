from game.shared.color import Color
import os

# Just a list of constants for reference elsewhere, nothing to see here.
COLUMNS = 40
ROWS = 40
CELL_SIZE = 25
MAX_X = 1000
MAX_Y = 1000
FRAME_RATE = 60
FONT_SIZE = 25
CAPTION = "Team 9's Platformer"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

LEVEL1 = os.path.dirname(os.path.abspath(__file__)) + "/data/level1.txt"
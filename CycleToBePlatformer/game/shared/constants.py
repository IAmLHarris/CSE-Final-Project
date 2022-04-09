from game.shared.color import Color
import os

# Just a list of constants for reference elsewhere, nothing to see here.
COLUMNS = 32
ROWS = 32
CELL_SIZE = 16
MAX_X = 512
MAX_Y = 512
FRAME_RATE = 48
FONT_SIZE = 25
CAPTION = "Team 6's Platformer"
SNAKE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
ORANGE = Color(255, 165, 0)
GRAY = Color(50, 50, 50)

LEVEL1 = os.path.dirname(os.path.abspath(__file__)) + "/data/level1.txt"
LEVEL2 = os.path.dirname(os.path.abspath(__file__)) + "/data/level2.txt"
LEVEL3 = os.path.dirname(os.path.abspath(__file__)) + "/data/level3.txt"

MAX_SPEED_NORTH = 13
MAX_SPEED_EAST = 7
MAX_SPEED_SOUTH = 10
MAX_SPEED_WEST = 7
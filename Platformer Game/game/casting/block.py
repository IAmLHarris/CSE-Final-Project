import random


from game.shared import constants as constants
from game.casting.actor import Actor
from game.shared.point import Point


class Block(Actor):
    """
    A square that the player can walk on or bump into.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, x=0, y=0, color = constants.GREEN):
        "Constructs a new block."
        super().__init__()
        self._points = 0
        self.set_text("O")
        self.set_color(color)
        self.set_font_size(constants.FONT_SIZE)
        position = Point(x, y)
        self.set_position(position)
        # self.reset()
        
    # def block_pop_reset(self, location):
    #     """Selects a random position and points that the food is worth."""
    #     ### self._points = random.randint(1, 8)

    #     x = random.randint(1, constants.COLUMNS - 1)
    #     y = random.randint(1, constants.ROWS - 1)
    #     position = Point(x, y)
    #     position = position.scale(constants.CELL_SIZE)
    #     self.set_position(position)
        
    # def get_points(self):
    #     """Gets the points the food is worth.
        
    #     Returns:
    #         points (int): The points the food is worth.
    #     """
    #     return self._points
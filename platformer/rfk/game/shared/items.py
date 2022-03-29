from game.shared.color import Color
from game.shared.point import Point

class Item:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of item is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new item."""
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_item_position(self):
        """Gets the item's position in 2d space.
        
        Returns:
            Point: The item's position in 2d space.
        """
        return self._position
    
    def get_item_text(self):
        """Gets the item's textual representation.
        
        Returns:
            string: The item's textual representation.
        """
        return self._text

    def get_item_velocity(self):
        """Gets the item's speed and direction.
        
        Returns:
            Point: The item's speed and direction.
        """
        return self._velocity
    

    def set_item_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_item_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_item_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
from game.shared import constants as constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._player_direction = Point(0, -constants.CELL_SIZE)
        # self._blue_direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        player = cast.get_first_actor("player")

        velocity = player.get_velocity()
        
        dx = velocity.get_x()
        dy = velocity.get_y()

        # left
        if self._keyboard_service.is_key_down('a'):
            dx += -1
            
        
        # right
        if self._keyboard_service.is_key_down('d'):
            dx += 1

        
        # down
        if self._keyboard_service.is_key_down('s'):
            dy += 1

        
        direction = Point(dx, dy)

        

        # Jumping! If you're standing on a platform, you can jump!
        collision_south = player.get_south_colliding_boolean()

        if collision_south:
            # jump

            if self._keyboard_service.is_key_down('space'):
                dy += -5

        # Gravity! If you're not standing on a platform, then you fall!
        if not collision_south:
            if dy <= 5:
                dy += 1
            else:
                print("Gravity isn't working right now.")

            # player.set_velocity(velocity)


        # velocity = velocity.add(Point(dx, dy))

        # player.set_velocity(velocity)
        player.set_velocity(Point(dx, dy))
    
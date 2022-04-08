from this import d
from game.shared.constants import MAX_SPEED_EAST, MAX_SPEED_NORTH, MAX_SPEED_SOUTH, MAX_SPEED_WEST, CELL_SIZE

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
        self._player_direction = Point(0, -CELL_SIZE)
        # self._blue_direction = Point(0, -CELL_SIZE)

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

        collision_north = player.get_north_colliding_variable()
        collision_east = player.get_east_colliding_variable()
        collision_south = player.get_south_colliding_variable()
        collision_west = player.get_west_colliding_variable()

        # LEFT ---------------------

        # Moving left when you press "a"
        if dx > -MAX_SPEED_WEST and self._keyboard_service.is_key_down('a'):
            dx += -1


        # Stopping moving left when you let go of "a"
        if dx < 0 and not self._keyboard_service.is_key_down("a"):
            dx += 1
            

        # RIGHT ----------------------
        
        # Moving right when you press "d"
        if dx < MAX_SPEED_EAST:
            if self._keyboard_service.is_key_down('d'):
                dx += 1

        # Stopping moving right when you let go of "d"
        if dx > 0 and not self._keyboard_service.is_key_down("d"):
            dx += -1
        

        # JUMPING --------------------

        # Jumping! If you're standing on a platform, you can jump!
        if collision_south == True and self._keyboard_service.is_key_down('space'):
            dy += -MAX_SPEED_NORTH


        # GRAVITY --------------------

        # Gravity! If you're not standing on a platform, then you fall!
        if collision_south == False:
            if dy < MAX_SPEED_SOUTH:
                dy += 1
                # print("Gravity!")
            else:
                # print("Gravity isn't working right now.")
                pass


        

        # South Collision! If you're standing on a block, then you stop moving down.
        # If you're going to run into a block, then you move up to it, and don't go past.
        if collision_south <= MAX_SPEED_SOUTH and dy >= collision_south and collision_south != False:
            dy = collision_south - 1

        # East Collision!
        if collision_east <= MAX_SPEED_EAST and dx >= collision_east and collision_east != False:
            dx = collision_east + 1

        # North Collision!
        if collision_north <= MAX_SPEED_NORTH and -dy >= collision_north and collision_north != False:
            dy = collision_north + 1

        # West Collision!
        if collision_west <= MAX_SPEED_WEST and -dx >= collision_west and collision_west != False:
            dx = collision_west + 1

        # print(f"South collision: {collision_south} | dy: {dy}")

        player.set_velocity(Point(dx, dy))

        # # Troubleshooting lines:
        # current_position = player.get_position()
        # current_x_position = current_position.get_x()
        # print(current_x_position)
    
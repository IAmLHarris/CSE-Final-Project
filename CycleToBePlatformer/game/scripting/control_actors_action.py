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

        # LEFT ---------------------

        # Moving left when you press "a"
        if dx >= -MAX_SPEED_WEST and self._keyboard_service.is_key_down('a'):
            dx += -1


        # Stopping moving left when you let go of "a"
        if dx < 0 and not self._keyboard_service.is_key_down("a"):
            dx += 1
            

        # RIGHT ----------------------
        
        # Moving right when you press "d"
        if dx <= MAX_SPEED_EAST:
            if self._keyboard_service.is_key_down('d'):
                dx += 1

        # Stopping moving right when you let go of "d"
        if dx > 0 and not self._keyboard_service.is_key_down("d"):
            dx += -1
        

        # JUMPING --------------------

        # Jumping! If you're standing on a platform, you can jump!
        collision_south = player.get_south_colliding_variable()

        if collision_south == True and self._keyboard_service.is_key_down('space'):
            dy += -MAX_SPEED_NORTH


        # GRAVITY --------------------

        # Gravity! If you're not standing on a platform, then you fall!
        if collision_south == False:
            if dy <= MAX_SPEED_SOUTH:
                dy += 1
                # print("Gravity!")
            else:
                # print("Gravity isn't working right now.")
                pass


        if collision_south <= MAX_SPEED_SOUTH and dy >= collision_south and collision_south != False:
            dy = collision_south - 1

        # Collision with something below you! If you're standing on a platform, you stop falling!
        # if collision_south and dy >= 0:
        #     dy = 0
            # print("Direct collision south")

        # elif collision_south == 1 and dy >= 1:
        #     dy = 1
        #     # print("Collision south 1")

        # elif collision_south == 2 and dy >= 2:
        #     dy = 2
        #     # print("Collision south 2")

        # elif collision_south == 3 and dy >= 3:
        #     dy = 3
        #     # print("Collision south 3")

        # elif collision_south == 4 and dy >= 4:
        #     dy = 4
        #     # print("Collision south 4")

        # elif collision_south == 5 and dy >= 5:
        #     dy = 5
        #     # print("Collision south 5")

        # else:
            # print("No collision south")

        print(f"South collision: {collision_south} | dy: {dy}")



        # velocity = velocity.add(Point(dx, dy))

        # player.set_velocity(velocity)
        player.set_velocity(Point(dx, dy))
    
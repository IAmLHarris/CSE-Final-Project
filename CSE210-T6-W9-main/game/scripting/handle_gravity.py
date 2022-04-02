from game.scripting.action import Action
from game.shared.point import Point
# from game.casting.cycle import cycle

class HandleGravity(Action):
    """
    An update action that handles gravity of the player actor.
    
    The responsibility of HandleGravity is to handle the constant downward velocity of the player
    at regular intervals when the player is not on top of solid ground.
    """

    
    def __init__(self):
        """Constructs a new HandleGravityAction."""
        self.game_timer = 0

    def execute(self, cast, script):
        """Executes the handle gravity action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self.game_timer += 1
        player = cast.get_first_actor("player")
        dy = 0
        dx = 0


        ### game_over = cast.get_first_actor("messages")
        
        

        # The growth of the cycles is determined by this value. 1 = every frame, 2 = every other frame, 15 = every second, 30 = every other second, etc.
        #                    V
        if self.game_timer % 5 == 0:
            y += -1
            print(self.game_timer)
            print(y)
            # print("my skeleton is ash")
            # print(direction)
            direction = Point(0, y)
            player.turn_head(direction)
            # cycle2 = cycles[1]

            # cycle1.grow_tail(1)
            # cycle2.grow_tail(1)


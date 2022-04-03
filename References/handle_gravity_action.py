from game.shared.point import Point
from game.scripting.action import Action
# from game.casting.cycle import cycle

class HandleGravityAction(Action):
    """
    An update action that handles growth of the cycle actors.
    
    The responsibility of HandleGrowthAction is to handle the growth of the tail of each cycle
    at regular intervals when the game is going.
    """

    
    def __init__(self):
        """Constructs a new HandleGrowthAction."""
        self.game_timer = 0
        self.dy = 0

    def execute(self, cast, script):
        """Executes the handle growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self.game_timer += 1
        
        self.dy += 1
        player = cast.get_first_actor("player")

        player.gravity()

        colliding_below = player.get_south_colliding_boolean()
        
        # if self.game_timer % 1 == 0 and colliding_below == False:
            # player.gravity()

            

            
            


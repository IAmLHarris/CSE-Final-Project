from game.shared.constants import CELL_SIZE
from game.shared import constants as constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when a cycle collides
    with another cycle or with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, cast):
        """Constructs a new HandleCollisionsAction."""
        
        print(f"collision {cast}")
        
        
        
        self._is_game_over = False
        self._red_wins = "who cares"

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            
            self._handle_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of it or it's opponent's segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player = cast.get_first_actor("player")
        blocks = cast.get_actors("blocks")

        player_position = player.get_position()
        below_player_hitbox = player_position.add(Point(0, (CELL_SIZE / 2)))
        # forgot = wonder.add(Point(0, 0))
        # print(forgot.get_x())
        

        # print(blocks.get_position().get_x())

        for block in blocks:
            
            block.get_position().get_x()
            if block.get_position().equals(below_player_hitbox):
                # This is for the south collision of the player. Use the add thing in line 50 to change the offset.
                player.set_south_colliding_boolean(True)
            elif not block.get_position().equals(below_player_hitbox):
                player.set_south_colliding_boolean(False)







        # player.get_position()
        # print(f"PX: {player.get_x()}")
        # print(f"PY: {player.get_y()}\n")
        # cycle1 = cycles[0]
        # # cycle2 = cycles[1]

        # head1 = cycle1.get_segments()[0]
        # segment1 = cycle1.get_segments()[1:]

        # # head2 = cycle2.get_segments()[0]
        # # segment2 = cycle2.get_segments()[1:]
        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the losing cycle white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over == True:
            
            cycles = cast.get_actors("cycles")

            # cycle1 = cycles[0]
            # cycle2 = cycles[1]

            if self._red_wins == True:
                player_color = "Red"
                cycle = cycles[1]
                
            # else:
            #     player_color = "Blue"
            #     cycle = cycles[0]

            
            segments = cycle.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"{player_color} wins! Game over.")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            # food.set_color(constants.WHITE)
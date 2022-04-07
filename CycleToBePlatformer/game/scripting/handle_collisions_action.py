from game.shared.constants import CELL_SIZE, MAX_SPEED_EAST, MAX_SPEED_NORTH, MAX_SPEED_SOUTH, MAX_SPEED_WEST
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


        # Change the offsets for how far below the player we check for collision:

        # below_player_hitbox = player_position.add(Point(0, (CELL_SIZE)))
        # below_player_hitbox_x = below_player_hitbox.get_x()
        # below_player_hitbox_y = below_player_hitbox.get_y()
        player_coordinates = player_position
        player_x = player_coordinates.get_x()
        player_y = player_coordinates.get_y()


        


        # forgot = wonder.add(Point(0, 0))
        # print(forgot.get_x())
        

        # print(blocks.get_position().get_x())

        colliding_with_at_least_one_block_south = False
        closest_block_south_y = False

        for block in blocks:
            block_position = block.get_position()
            block_x = block_position.get_x()
            block_y = block_position.get_y()
            block.get_position().get_x()

            


            # Rewriting south collision:
            if ((block_y - player_y >= 0) and (block_y - player_y <= MAX_SPEED_SOUTH))    and    ((player_x <= block_x + (CELL_SIZE / 2)) and (player_x >= block_x - (CELL_SIZE / 2))):
                if closest_block_south_y == False or closest_block_south_y < block_y:
                    player.set_south_colliding_variable(block_y - player_y)
                    colliding_with_at_least_one_block_south = True
                    closest_block_south_y = block_y
            
            elif colliding_with_at_least_one_block_south == False:
                player.set_south_colliding_variable(False)


            # # Old South collision:
            # if below_player_hitbox_y == block_y and below_player_hitbox_x <= block_x + (CELL_SIZE / 2) and below_player_hitbox_x >= block_x - (CELL_SIZE / 2):
                
            #     player.set_south_colliding_variable(True)
            #     colliding_with_at_least_one_block_south = True
            
            # # South collision soon, 1 px away:
            # elif below_player_hitbox_y + 1 == block_y and below_player_hitbox_x <= block_x + (CELL_SIZE / 2) and below_player_hitbox_x >= block_x - (CELL_SIZE / 2):
            #     player.set_south_colliding_variable(1)
            #     colliding_with_at_least_one_block_south = True

            # # South collision soon, 2 px away:
            # elif below_player_hitbox_y + 2 == block_y and below_player_hitbox_x <= block_x + (CELL_SIZE / 2) and below_player_hitbox_x >= block_x - (CELL_SIZE / 2):
            #     player.set_south_colliding_variable(2)
            #     colliding_with_at_least_one_block_south = True

            # # South collision soon, 3 px away:
            # elif below_player_hitbox_y + 3 == block_y and below_player_hitbox_x <= block_x + (CELL_SIZE / 2) and below_player_hitbox_x >= block_x - (CELL_SIZE / 2):
            #     player.set_south_colliding_variable(3)
            #     colliding_with_at_least_one_block_south = True

            # # South collision soon, 4 px away:
            # elif below_player_hitbox_y + 4 == block_y and below_player_hitbox_x <= block_x + (CELL_SIZE / 2) and below_player_hitbox_x >= block_x - (CELL_SIZE / 2):
            #     player.set_south_colliding_variable(4)
            #     colliding_with_at_least_one_block_south = True

            # elif not block.get_position().equals(below_player_hitbox) and not colliding_with_at_least_one_block_south:
            #     player.set_south_colliding_variable(False)

        
        
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
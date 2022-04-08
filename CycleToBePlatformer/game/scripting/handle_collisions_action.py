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
        
        
        
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
            
        self._handle_collision(cast)
        # self._handle_game_over(cast)
    
    def _handle_collision(self, cast):
        """Sets the game over flag if a cycle collides with one of it or it's opponent's segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player = cast.get_first_actor("player")
        blocks = cast.get_actors("blocks")

        player_position = player.get_position()


        # These set 
        player_coordinates = player_position
        player_x = player_coordinates.get_x()
        player_y = player_coordinates.get_y()

        

        # print(blocks.get_position().get_x())

        colliding_with_at_least_one_block_north = False
        colliding_with_at_least_one_block_east = False
        colliding_with_at_least_one_block_south = False
        colliding_with_at_least_one_block_west = False
    
        closest_block_north_y = False
        closest_block_east_x = False
        closest_block_south_y = False
        closest_block_west_x = False

        for block in blocks:
            block_position = block.get_position()
            block_x = block_position.get_x()
            block_y = block_position.get_y()
            block.get_position().get_x()

            


            # South Collision! Rewritten in version 0.020 for better maintainability.
            block_y_adjusted_for_south_collision = block_y - CELL_SIZE
            if ((block_y_adjusted_for_south_collision - player_y >= 0) and (block_y_adjusted_for_south_collision - player_y <= MAX_SPEED_SOUTH))    and    ((player_x <= block_x + (CELL_SIZE / 2)) and (player_x >= block_x - (CELL_SIZE / 2))):
                if closest_block_south_y == False or closest_block_south_y < block_y_adjusted_for_south_collision:
                    player.set_south_colliding_variable(block_y_adjusted_for_south_collision - player_y)
                    colliding_with_at_least_one_block_south = True
                    closest_block_south_y = block_y_adjusted_for_south_collision
                    
            
            elif colliding_with_at_least_one_block_south == False:
                player.set_south_colliding_variable(False)

            # West Collision! Written in version 0.021 based off of south collision.
            block_x_adjusted_for_west_collision = block_x + CELL_SIZE
            if ((player_x - block_x_adjusted_for_west_collision >= 0) and (player_x - block_x_adjusted_for_west_collision <= MAX_SPEED_WEST))    and    ((player_y <= block_y + (CELL_SIZE / 2)) and (player_y >= block_y - (CELL_SIZE / 2))):
                if closest_block_west_x == False or closest_block_west_x > block_x_adjusted_for_west_collision:
                    player.set_west_colliding_variable(block_x_adjusted_for_west_collision - player_x)
                    colliding_with_at_least_one_block_west = True
                    closest_block_west_x = block_x_adjusted_for_west_collision
                    print("Just activated West Collision")
            
            elif colliding_with_at_least_one_block_west == False:
                player.set_west_colliding_variable(False)


            # East collision. Written in version 0.022 for the sake of understanding what's going wrong with West collision.
            block_x_adjusted_for_east_collision = block_x - CELL_SIZE
            if ((block_x_adjusted_for_east_collision - player_x >= 0) and (block_x_adjusted_for_east_collision - player_x <= MAX_SPEED_EAST))    and    ((player_y <= block_y + (CELL_SIZE / 2)) and (player_y >= block_y - (CELL_SIZE / 2))):
                if closest_block_east_x == False or closest_block_east_x < block_x_adjusted_for_east_collision:
                    print(block_x_adjusted_for_east_collision + player_x)
                    player.set_east_colliding_variable(block_x_adjusted_for_east_collision - player_x)
                    print(block_x_adjusted_for_east_collision + player_x)
                    colliding_with_at_least_one_block_east = True
                    closest_block_east_x = block_x_adjusted_for_east_collision
                    print("Just activated East Collision")
                    
            
            elif colliding_with_at_least_one_block_east == False:
                player.set_east_colliding_variable(False)

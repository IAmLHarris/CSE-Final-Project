from game.shared import constants as constants
# from game.shared.constants import constants as Constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_growth_action import HandleGrowthAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())
    # cast.add_actor("snakes", Snake())
    # cast.add_actor("red cycle", Snake())
    # cast.add_actor("blue cycle", Snake())

    cycle_one = Cycle()
    cycle_two = Cycle()
    
    score_one = Score("One")
    score_two = Score("Two")
    
    cycle_one.prepare_body(constants.RED)
    cycle_two.prepare_body(constants.BLUE)

    cast.add_actor("cycles", cycle_one)
    cast.add_actor("cycles", cycle_two)
    
    score_one.prepare_score("One")
    score_two.prepare_score("Two")
    
    cast.add_actor("scores", score_one)
    cast.add_actor("scores", score_two)
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", HandleGrowthAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()


# # cast.add_actor("cycles", Snake())
# # cast.add_actor("cycles", Snake())

# #-----

# cycles = cast.get_all_actors("cycles")

# red_cycle = cycles[0]
# blue_cycle = cycles[1]


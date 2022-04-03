from hashlib import new
from tkinter import font
from game.shared.constants import LEVEL1
from game.scripting.action import Action
from game.casting.block import Block
from game.shared.point import Point
from game.shared.constants import BLUE, FONT_SIZE
from game.casting.cast import Cast
import os

class PopulateBlockCastAction(Action):
    """
    An action that will populate the cast with the needed blocks for the level.
    
    The PopulateBlockCastAction is here to load the blocks in our level, putting them in the cast for the rest of our cast to interact with. 
    It should be called at the beginning of the game, and whenever the player crosses into a new level.
    """

    
    # def __init__(self):
    #     """Constructs a new PopulateBlockCastAction."""
    #     self.test = 0

    def __init__(self, level_data):
        """Executes populate block cast action.

        Args:
            cast (Cast): The cast of Actors in the game.
            resources (Resources): The non-cast resources needed to run the game reliably.
            script (Script): The script of Actions in the game.
        """
        # level = resources.get_first_item("level")
        cast = Cast()
        # print("opening")
        with open(level_data) as level:
            level_data = level.read()
            level_lines = level_data.splitlines()
            
            # print(f"level_lines: \n{level_lines}")

            self.blocks = []
            
            
            for block in level_lines:
                list_count=0
                

                
                # print("Adding block to list in PopulateBlockCastAction")
                if ("#" in block and "block " not in block) or block == "":
                    # print(f"Casting out invalid block: \n{block}")
                    pass

                elif "#" not in block and "block " in block:
                    # print(f"Accepting valid block: \n{block}")

                    stripped_block=block.strip(".")
                    split_block=stripped_block.split()
                    # print(split_block)

                    self.blocks.append(split_block)

                    
                    
                    # x = split_block[1]
                    # y = split_block[2]

                    # new_block = Block()
                    
                    # Covering all my bases for testing:
                    # print(f"x: {x}, y: {y}")
                    # new_block.set_color(BLUE)
                    # new_block.set_font_size(FONT_SIZE)
                    # new_block.set_text("O")
                

                    
                    # new_block.set_position(Point(x, y))
                    # cast.add_actor("blocks", new_block)
                    # self.why_must_you_do_this = cast.get_actors("blocks")
                    
                    # This line above should basically be cast.add_item("blocks", new_block)
                    # Need to check and see if that's the right way to phrase it.

                else:
                    print("There was a logic error in determining whether the block was valid or not:")
                    print(block)
                    pass

    def get_populated_block_cast(self):
        # print(self.blocks)
        return self.blocks

            




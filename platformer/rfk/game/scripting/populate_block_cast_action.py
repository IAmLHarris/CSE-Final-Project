from game.scripting.action import Action
import os

class PopulateBlockCastAction(Action):
    """
    An action that will populate the cast with the needed blocks for the level.
    
    The PopulateBlockCastAction is here to load the blocks in our level, putting them in the cast for the rest of our cast to interact with. 
    It should be called at the beginning of the game, and whenever the player crosses into a new level.
    """

    
    def __init__(self):
        """Constructs a new PopulateBlockCastAction."""
        self.level = 0

    def execute(self, cast, resources, script):
        """Executes populate block cast action.

        Args:
            cast (Cast): The cast of Actors in the game.
            resources (Resources): The non-cast resources needed to run the game reliably.
            script (Script): The script of Actions in the game.
        """
        # level = resources.get_first_item("level")

        with open(os.path.dirname(os.path.abspath(__file__)) + "/data/level1.txt") as level:
            level_data = level.read()
            level_lines = level_data.splitlines()
            
            print(f"level_lines: \n{level_lines}")

            blocks = []
            
            for block in level_lines:
                list_count=0
                print("Adding block to list in PopulateBlockCastAction")
                if "#" in block and "block," not in block:
                    print(f"Casting out invalid block: \n{block}")

                elif "#" not in block and "block," in block:
                    print(f"Accepting valid block: \n{block}")
                    blocks.append(block)

                else:
                    print("There was a logic error in determining whether the block was valid or not.")


                

        # This section should take each line from the level (the level I think should be a string variable with the file path) 
        # and load it up if it's a block, or something like that.

if __name__ == "__main__":
    PopulateBlockCastAction = PopulateBlockCastAction
    PopulateBlockCastAction.execute(0, 0, 0)



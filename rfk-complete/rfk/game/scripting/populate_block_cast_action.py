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
            blocks = level_data.splitlines()
            
            
            for block in blocks:
                list_count=0
                print("i'm doing a thing")
                if "#" in block:
                    blocks.pop(list_count)
                    print("I DID A THING")

                




        # This section should take each line from the level (the level I think should be a string variable with the file path) 
        # and load it up if it's a block, or something like that.



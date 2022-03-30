from platformer.game.scripting.action import Action

class set_robot_velocity_action(Action):
    
    def __init__(self):
        pass


    def execute(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("player character")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        
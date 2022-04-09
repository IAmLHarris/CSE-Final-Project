# from constants import Constants
# from turtle import pos, position

from game.shared.constants import FONT_SIZE, WHITE, ORANGE
from game.shared import constants as constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    Player Character
    
    The responsibility of the player character actor is to be a vessel for the player. 

    """
    def __init__(self):
        """Constructs a new Cycle actor."""
        super().__init__()
        self.set_text("Q")
        self.set_font_size(FONT_SIZE)
        self.set_color(ORANGE)
        self.grav_counter = 0
        self.prepare_body()
        self.north_colliding_variable = False
        self.east_colliding_variable = False
        self.south_colliding_variable = False
        self.west_colliding_variable = False


    def prepare_body(self):
        x = int(50)
        y = int(460)
        position = Point(x, y)
        self.set_position(position)

    def set_direction(self, position):
        """Changes the direction that the player is going. """
        self.set_velocity(position)


    def get_colliding_variables(self):
        """Returns a variable if whether or not the player is colliding"""
        return (self.north_colliding_variable, self.east_colliding_variable, self.south_colliding_variable, self.west_colliding_variable)

    def get_north_colliding_variable(self):
        return self.north_colliding_variable

    def get_east_colliding_variable(self):
        return self.east_colliding_variable

    def get_south_colliding_variable(self):
        return self.south_colliding_variable

    def get_west_colliding_variable(self):
        return self.west_colliding_variable


    def set_colliding_variables(self, value):
        """Returns all variables as to whether the player is colliding with something in each given direction"""
        self.north_colliding_variable = value[0]
        self.east_colliding_variable = value[1]
        self.south_colliding_variable = value[2]
        self.west_colliding_variable = value[3]

    def set_north_colliding_variable(self, value):
        """Returns a variable as to whether or not the player is colliding with something above them"""
        self.north_colliding_variable = value
    
    def set_east_colliding_variable(self, value):
        """Returns a variable as to whether or not the player is colliding with something to the right of them"""
        self.east_colliding_variable = value
    
    def set_south_colliding_variable(self, value):
        """Returns a variable as to whether or not the player is colliding with something below them"""
        self.south_colliding_variable = value

    def set_west_colliding_variable(self, value):
        """Returns a variable as to whether or not the player is colliding with something to the left of them"""
        self.west_colliding_variable = value



    # def move_next(self):
    #     """Moves every segment in the cycle"""
    #     # move all segments
    #     for segment in self._segments:
    #         segment.move_next()
    #     # update velocities
    #     for i in range(len(self._segments) - 1, 0, -1):
    #         trailing = self._segments[i]
    #         previous = self._segments[i - 1]
    #         velocity = previous.get_velocity()
    #         trailing.set_velocity(velocity)

    # def get_head(self):
    #     """Returns the first segment of the cycle"""
    #     return self._segments[0]

    # def gravity(self):
    #     """it's gravity, and it doesn't take any arguments, just makes you go down a pixel each time it's activated"""

        # velocity = self.get_velocity()

        # if velocity.get_y() <= 5:
        #     velocity = velocity.add(Point(0, 1))
        # else:
        #     print("Gravity isn't working right now.")

        # self.set_velocity(velocity)

        # player_position = self.get_position()
        # gravity_doing_its_thing = Point(0, self.grav_counter)
        # position = player_position.add(gravity_doing_its_thing)

        # self.grav_counter += 1
        # self.set_position(position)


        # OLD CODE FROM PREVIOUS PROGRAMS:

        # print(f"PX: {player_position.get_x()}")
        # print(f"PY: {player_position.get_y()}\n")
        # print(f"GY{gravity_doing_its_thing.get_y}")
        # print(f"GC{self.grav_counter}\n")
        # print(f"NX: {position.get_x()}")
        # print(f"NY: {position.get_y()}\n")
        # print(position)
        # print(player_position)
        

    # def turn_head(self, velocity):
    #     """Turns the the cycle by changing the velocity of the head."""
    #     self._segments[0].set_velocity(velocity)
    
    # def prepare_body(self, color):
    #     """Prepares the body of the cycle"""

    #     self._cycle_color = color
    #     if color == constants.RED:
    #         x = int(constants.MAX_X / 2 - 10 * constants.CELL_SIZE)
    #         y = int(constants.MAX_Y / 2)

    #     elif color == constants.BLUE:
    #         x = int(constants.MAX_X / 2 + 10 * constants.CELL_SIZE)
    #         y = int(constants.MAX_Y / 2)

    #     else:
    #         x = int(constants.MAX_X / 2)
    #         y = int(constants.MAX_Y / 2)
    #         print("Something went wrong in finding the color of the cycle. game->casting->cycle.py->prepare_body")

    #     for i in range(constants.SNAKE_LENGTH):
    #         position = Point(x, y + i * constants.CELL_SIZE)
    #         velocity = Point(0, -1 * constants.CELL_SIZE)
    #         text = "8" if i == 0 else "#"

    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text(text)
    #         segment.set_color(color)
    #         self._segments.append(segment)
        


    
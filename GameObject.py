from cons import *
from images import *
from View import WALL_POSITIONS, GRASS_POSITIONS, BRICK_POSITIONS
from Shot import Shot


class GameObject:
    """
    Super class of the game objects: Player and Opponents.

    Attributes
    ----------
    position = tuple
    image = Surface
    img_dict = dictionary

    Methods:
    --------
    view_game_object(screen):
        Display object.
    turn(direction_key, game_object_one_list, game_object_two_list):
        Handle game object's turnover.
    create_shot(direction):
        Create a Shot object and return it.
    """

    def __init__(self):
        """
        Parameters
        ----------
        position : tuple
            The position of game object.
        image : Surface
            The image of game object.
        img_dict : dictionary
            The dictionary containing key direction: image of game object moving in that key direction.
        """

        self.position = (224, 416)
        self.image = player_up_image
        self.img_dict = {'UP': player_up_image,
                         'DOWN': player_down_image,
                         'RIGHT': player_right_image,
                         'LEFT': player_left_image}

    def view_game_object(self, screen):
        """
        Display object.

        Parameters
        ----------
        screen : pygame.Surface
            Game object is drawn on the screen.
        """

        screen.blit(self.image, self.position)

    def turn(self, direction_key, game_object_one_list, game_object_two_list):
        """
        Handle game object's turnover.
        If game object wants to go towards the wall, nothing is nothing changes.
        If game object wants to go towards the box with the wall or another box behind, only the picture changes.
        Else game object image and position changes.

        Parameters
        ----------
        direction_key: str
            String that describes the direction: 'UP', 'DOWN', 'RIGHT', 'LEFT'.
        game_object_one_list: list
            List of game objects.
        game_object_two_list: list
            List of game objects.
        """

        image = self.img_dict[direction_key]
        direction = DIRECTIONS[direction_key]
        game_object_one_positions_list = [object_one.position for object_one in game_object_one_list]
        game_object_two_positions_list = [object_two.position for object_two in game_object_two_list]

        position_x, position_y = self.position
        direction_x, direction_y = direction
        new_position = (position_x + direction_x, position_y + direction_y)
        new_position_x, new_position_y = new_position
        if new_position in WALL_POSITIONS or new_position in BRICK_POSITIONS:
            self.image = image
            return
        if game_object_one_list and new_position == game_object_one_positions_list[-1]:
            self.image = image
            return
        if game_object_two_list and new_position == game_object_two_positions_list[-1]:
            self.image = image
            return
        if new_position in GRASS_POSITIONS:
            self.position = new_position
        if new_position_y == -32 or new_position_y == 448:
            self.image = image
            return
        if new_position_x == -32 or new_position_x == 416:
            self.image = image
            return
        self.image = image
        self.position = new_position

    def create_shot(self, direction_key):
        """
        Create a Shot object and return it.

        Parameters
        ----------
        direction_key: str
            String that describes the direction: 'UP', 'DOWN', 'RIGHT', 'LEFT'.
        """

        return Shot(self.position, direction_key)

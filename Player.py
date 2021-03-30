from GameObject import GameObject
from images import *


class Player(GameObject):
    """
    Player class inherits from class Game Object.

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

        super().__init__()
        self.position = (224, 416)
        self.image = player_up_image
        self.img_dict = {'UP': player_up_image,
                         'DOWN': player_down_image,
                         'RIGHT': player_right_image,
                         'LEFT': player_left_image}

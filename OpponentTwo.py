from images import opponent_2_down_image, opponent_2_up_image, opponent_2_right_image, opponent_2_left_image
import random
from View import OPPONENT_POSITIONS
from Opponent import Opponent


class OpponentTwo(Opponent):
    """
    OpponentOne class inherits from class Opponent.

    Attributes
    ----------
    position = tuple
    image = Surface
    img_dict = dictionary
    direction_key = str

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
        direction_key : str
            String that describes the direction: 'UP', 'DOWN', 'RIGHT', 'LEFT'.
        """

        super().__init__()
        self.position = random.choice(OPPONENT_POSITIONS)
        self.image = opponent_2_down_image
        self.img_dict = {'UP': opponent_2_up_image,
                         'DOWN': opponent_2_down_image,
                         'RIGHT': opponent_2_right_image,
                         'LEFT': opponent_2_left_image}

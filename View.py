import pygame
from cons import BLACK, BLUE, LIGHT_GREEN, PICTURE_EDGE, map_level_1
from images import wall_image, grass_image, brick_image, flash_img_dict, smoke_img_dict

WALL_POSITIONS = []
GRASS_POSITIONS = []
BRICK_POSITIONS = []
OPPONENT_POSITIONS = []


class View:
    """
    Display game board, headline, scores and winning text.
    Saves positions of objects in lists: WALL_POSITIONS, BLUE_STORE_POSITIONS, BLUE_TILES_POSITIONS.

    Attributes
    ----------
    (width, height) = (int, int)
    screen = pygame.Surface
    map_level = str

    Methods:
    --------
    view_board(screen=screen):
        Display board based on defined map.
    flash_effect(screen, position, direction_key):
        Display flash effect after breaking the brick.
    smoke_effect(screen, position, direction_key):
        Display smoke effect after destroying an opponent.
    winning(screen, points, max_points):
        Display text when the players wins.
    score(screen, points, dead_opponent_one, dead_opponent_two):
        Display score on a screen.
    """

    (width, height) = (417, 448)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('War of Tanks')
    screen.fill(BLACK)
    pygame.display.flip()

    map_level = map_level_1.splitlines()
    for row, line in enumerate(map_level):
        for column, value in enumerate(line):
            if value == 'w':
                WALL_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))
            elif value == 'g':
                GRASS_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))
            elif value == 'b':
                BRICK_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))
            else:
                OPPONENT_POSITIONS.append((column * PICTURE_EDGE, row * PICTURE_EDGE))

    def view_board(self, screen=screen):
        """
        Display board based on defined map.

        Parameters
        ----------
        screen: pygame.Surface
            Game object is drawn on the screen.
        """

        for position in WALL_POSITIONS:
            screen.blit(wall_image, position)
        for position in GRASS_POSITIONS:
            screen.blit(grass_image, position)
        for position in BRICK_POSITIONS:
            screen.blit(brick_image, position)

    def flash_effect(self, screen, position, direction_key):
        """
        Display flash effect after breaking the brick.

        Parameters
        ----------
        screen: pygame.Surface
            Game object is drawn on the screen.
        position:  tuple
            Position where flash effect will display.
        direction_key: str
            Direction of flash.
        """

        screen.blit(flash_img_dict[direction_key], position)

    def smoke_effect(self, screen, position, direction_key):
        """
        Display smoke effect after destroying an opponent.

        Parameters
        ----------
        screen: pygame.Surface
            Game object is drawn on the screen.
        position:  tuple
            Position where smoke effect will display.
        direction_key: str
            Direction of smoke.
        """

        screen.blit(smoke_img_dict[direction_key], position)

    def winning(self, screen, points, max_points):
        """
        Display text when the players wins.

        Parameters
        ----------
        screen: pygame.Surface
            Game object is drawn on the screen.
        points:  int
            Points scored by the player.
        max_points: int
            Maximum number of points a player can score.
        """

        my_font = pygame.font.SysFont('orange juice', 80)
        if points == max_points:
            winning_text = my_font.render('!!! YOU WON !!!', True, BLUE)
            screen.blit(winning_text, (2, 200))

    def score(self, screen, points, dead_opponent_one, dead_opponent_two):
        """
        Display score on a screen.

        Parameters
        ----------
        screen: pygame.Surface
            Game object is drawn on the screen.
        points:  int
            Points scored by the player.
        dead_opponent_one : int
            Number of dead OpponentOne.
        dead_opponent_two : int
            Number of dead OpponentTwo.
        """

        my_font = pygame.font.SysFont('Comic Sans MS', 14)
        score_text = my_font.render('Score: %s' % points, True, LIGHT_GREEN)
        dead_opponent_one_text = my_font.render('Blue tanks: %s' % dead_opponent_one, True, LIGHT_GREEN)
        dead_opponent_two_text = my_font.render('Green tanks: %s' % dead_opponent_two, True, LIGHT_GREEN)
        screen.blit(score_text, (320, 365))
        screen.blit(dead_opponent_one_text, (320, 380))
        screen.blit(dead_opponent_two_text, (320, 397))

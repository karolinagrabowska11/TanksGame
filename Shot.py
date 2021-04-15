from images import shot_up_image, shot_down_image, shot_right_image, shot_left_image
from sound import brick_destroy_sound, impact
from cons import DIRECTIONS
from View import WALL_POSITIONS, BRICK_POSITIONS


class Shot:
    """
    The class responsible for shot object, moving the shot, shots collisions with brick, wall and game objects:
    player and opponents. Display the shot.

    Attributes
    ----------
    x = int
    y = int
    position = tuple
    direction_key = str
    direction = tuple
    img_dict = dictionary
    image = Surface

    Methods:
    --------
    view_game_object(screen):
        Display object.
    move():
        Move the shot.
    shot_collisions(screen, view, shots_group, dead_opponent_one, dead_opponent_two,opponents_one_list,
                    opponents_two_list, brick_collision, opponent_two_collision):
        Check player shots collisions with brick, wall and game objects: opponents.
    shot_opponent_one_collision(self, screen, view, shots_group_opponent_one, player, brick_collision, player_collision,
                                lost_lives):
        Check opponent shots collisions with brick, wall and game objects: player.
    """

    def __init__(self, tank_position, direction_key):
        """
        Parameters
        ----------
        x : int
            The position of game object on x-axis.
        y : int
            The position of game object on y-axis.
        position : tuple
            The position of game object.
        direction_key : str
            String that describes the direction: 'UP', 'DOWN', 'RIGHT', 'LEFT'.
        direction : tuple
            Direction of movement of the game object.
        img_dict : dictionary
            The dictionary containing key direction: image of game object moving in that key direction.
        image : Surface
            The image of game object.
        """

        self.x, self.y = tank_position
        self.position = (self.x, self.y)
        self.direction_key = direction_key
        self.direction = DIRECTIONS[self.direction_key]
        self.img_dict = {'UP': shot_up_image,
                         'DOWN': shot_down_image,
                         'RIGHT': shot_right_image,
                         'LEFT': shot_left_image}
        self.image = self.img_dict[self.direction_key]

    def view_game_object(self, screen):
        """
        Display the shot.

        Parameters
        ----------
        screen : pygame.Surface
            Game object is drawn on the screen.
        """

        screen.blit(self.image, self.position)

    def move(self):
        """
        Move the shot.
        """

        direction_x, direction_y = self.direction
        self.x += direction_x
        self.y += direction_y
        self.position = (self.x, self.y)

    def shot_collisions(self, screen, view, shots_group, dead_opponent_one, dead_opponent_two,
                        opponents_one_list, opponents_two_list, brick_collision, opponent_two_collision):
        """
        Check player shots collisions with brick, wall and game objects: opponents.

        Parameters
        ----------
        screen : pygame.Surface
            Game object is drawn on the screen.
        view : View
            View object.
        shots_group: list
            List of Shot object.
        dead_opponent_one : int
            Number of dead OpponentOne.
        dead_opponent_two : int
            Number of dead OpponentTwo.
        opponents_one_list : list
            List of game objects OpponentOne.
        opponents_two_list : list
            List of game objects OpponentTwo.
        brick_collision : int
            Number of collisions with brick.
        opponent_two_collision :
            Number of collisions with object game OpponentTwo.

        Returns
        -------
        dead_opponent_one : int
            Number of dead OpponentOne.
        dead_opponent_two : int
            Number of dead OpponentTwo.
        brick_collision : int
            Number of collisions with brick.
        opponent_two_collision : int
            Number of collisions with object game OpponentTwo.
        """

        game_object_one_positions_list = [object_one.position for object_one in opponents_one_list]
        game_object_two_positions_list = [object_two.position for object_two in opponents_two_list]

        for s in range(len(shots_group)):
            shot_object = shots_group[s]
            shot_object.move()
            if shot_object.position in WALL_POSITIONS:
                shots_group.pop(0)
                break
            if shot_object.position in BRICK_POSITIONS:
                shots_group.pop(0)
                brick_collision += 1
                if brick_collision == 3:
                    BRICK_POSITIONS.remove(shot_object.position)
                    view.flash_effect(screen, shot_object.position, self.direction_key)
                    brick_collision = 0
                    brick_destroy_sound.play()
                break
            if game_object_one_positions_list:
                if shot_object.position == game_object_one_positions_list[-1]:
                    shots_group.pop(0)
                    dead_opponent_one += 1
                    view.smoke_effect(screen, shot_object.position, self.direction_key)
                    opponents_one_list.pop()
                    impact.play()
                    return dead_opponent_one, dead_opponent_two, brick_collision, opponent_two_collision
            if game_object_two_positions_list:
                if shot_object.position == game_object_two_positions_list[-1]:
                    shots_group.clear()
                    opponent_two_collision += 1
                    impact.play()
                    if opponent_two_collision == 2:
                        dead_opponent_two += 1
                        view.smoke_effect(screen, shot_object.position, self.direction_key)
                        opponents_two_list.pop()
                        opponent_two_collision = 0
                    return dead_opponent_one, dead_opponent_two, brick_collision, opponent_two_collision
            shot_object.view_game_object(screen)
        return dead_opponent_one, dead_opponent_two, brick_collision, opponent_two_collision

    def shot_opponent_one_collision(self, screen, view, shots_group_opponent_one, player, player_collision,
                                    player_lives, screen_delay):
        """
        Check opponent shots collisions with brick, wall and game objects: player.

        Parameters
        ----------
        screen : pygame.Surface
            Game object is drawn on the screen.
        view : View
            View object.
        shots_group_opponent_one: list
            List of Shot object.
        player : Player
            Player object.
        player_collision : int
            Number of collisions with object game Player.
        player_lives : int
            Number of Player's lost lives.
        screen_delay : bool
            Responsible for screen delay after shot collision with Player.

        Returns
        -------
        player_collision : int
            Number of collisions with object game Player.
        player_lives : int
            Number of Player's lost lives.
        screen_delay : bool
            Responsible for screen delay after shot collision with Player.
        """

        for s in range(len(shots_group_opponent_one)):
            shot_object = shots_group_opponent_one[s]
            shot_object.move()
            if shot_object.position in WALL_POSITIONS:
                shots_group_opponent_one.pop()
                break
            if shot_object.position in BRICK_POSITIONS:
                shots_group_opponent_one.pop()
                break
            if shot_object.position == player.position:
                shots_group_opponent_one.pop()
                player_collision += 1
                impact.play()
                if player_collision == 2:
                    player_lives -= 1
                    player.position = (224, 416)
                    view.smoke_effect(screen, shot_object.position, self.direction_key)
                    player_collision = 0
                    screen_delay = True
                    if player_lives == 0:
                        screen_delay = False
                return player_collision, player_lives, screen_delay
            shot_object.view_game_object(screen)
        return player_collision, player_lives, screen_delay

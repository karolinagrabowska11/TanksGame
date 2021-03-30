import pygame
import sys
import random
from cons import BLACK, DIRECTIONS_KEYS


class Game:
    """
    Class responsible for main game loop, handling keyboard.
    """

    def game_loop(self, clock, view, player, opponents_one_list, opponents_two_list, screen):
        """
        Main game loop, handling keyboard.

        Parameters
        ----------
        clock : pygame.Clock
            pygame.Clock object.
        view : View
            View object.
        player : Player
            Player object.
        opponents_one_list : list
            List of game objects OpponentOne.
        opponents_two_list : list
            List of game objects OpponentTwo.
        screen : pygame.Surface
            Game object is drawn on the screen.
        """

        init_status = pygame.init()
        if init_status[1] > 0:
            print('%s errors... Exiting...' % init_status[1])
            sys.exit()
        else:
            print('Welcome in PyGame - War of Tanks!')

        view.view_board()
        shot_direction = DIRECTIONS_KEYS[0]
        shots_group = []
        shots_group_opponent_one = []
        move_opponent_variable = 0
        dead_opponent_one = 0
        opponents_one_number = len(opponents_one_list)
        dead_opponent_two = 0
        opponents_two_number = len(opponents_two_list)
        max_points = opponents_one_number + opponents_two_number * 2
        brick_collision = 0
        opponent_two_collision = 0
        previous_time_player_shot = pygame.time.get_ticks()
        previous_time_opponent_one_shot = pygame.time.get_ticks()
        player_collision = 0
        lost_lives = 0
        shot = None

        while True:
            clock.tick(8)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                shot_direction = DIRECTIONS_KEYS[2]
                player.turn('RIGHT', opponents_one_list, opponents_two_list)
            elif keys[pygame.K_LEFT]:
                shot_direction = DIRECTIONS_KEYS[3]
                player.turn('LEFT', opponents_one_list, opponents_two_list)
            elif keys[pygame.K_UP]:
                shot_direction = DIRECTIONS_KEYS[0]
                player.turn('UP', opponents_one_list, opponents_two_list)
            elif keys[pygame.K_DOWN]:
                shot_direction = DIRECTIONS_KEYS[1]
                player.turn('DOWN', opponents_one_list, opponents_two_list)
            elif keys[pygame.K_SPACE]:
                current_time_player_shot = pygame.time.get_ticks()
                if current_time_player_shot - previous_time_player_shot > 500:
                    previous_time_player_shot = current_time_player_shot
                    shot = player.create_shot(shot_direction)
                    shots_group.append(shot)
            elif keys[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            # elif event.key == pygame.K_r:  # restart
            #     player.__init__()

            screen.fill(BLACK)

            if shot is not None:
                dead_opponent_one, dead_opponent_two, brick_collision, opponent_two_collision = shot.shot_collisions(
                    screen, view, shots_group, dead_opponent_one, dead_opponent_two, opponents_one_list,
                    opponents_two_list, brick_collision, opponent_two_collision)

            if move_opponent_variable == 7:
                if opponents_one_list:
                    opponents_one_list[-1].turn(random.choice(DIRECTIONS_KEYS), [player], opponents_two_list)
                if opponents_two_list:
                    opponents_two_list[-1].turn(random.choice(DIRECTIONS_KEYS), [player], opponents_one_list)
                move_opponent_variable = 0
            move_opponent_variable += 1

            # current_time_opponent_one_shot = pygame.time.get_ticks()
            # if opponents_one_list and current_time_opponent_one_shot - previous_time_opponent_one_shot > 1000:
            #     previous_time_opponent_one_shot = current_time_opponent_one_shot
            #     opponent_one_shot = opponents_one_list[-1].create_shot(opponents_one_list[-1].direction_key)
            #     shots_group_opponent_one.append(opponent_one_shot)
            #     brick_collision, player_collision, lost_lives = opponent_one_shot.shot_opponent_one_collision(screen,
            #                                                                                                   view,
            #                                                                                                   shots_group_opponent_one,
            #                                                                                                   player,
            #                                                                                                   brick_collision,
            #                                                                                                   player_collision,
            #                                                                                                   lost_lives)

            player.view_game_object(screen)

            if dead_opponent_one < opponents_one_number:
                opponents_one_list[-1].view_game_object(screen)
            if dead_opponent_two < opponents_two_number:
                opponents_two_list[-1].view_game_object(screen)

            view.view_board(screen)
            points_sum = dead_opponent_one * 1 + dead_opponent_two * 2
            view.score(screen, points_sum, dead_opponent_one, dead_opponent_two)
            view.winning(screen, points_sum, max_points)
            pygame.display.update()

from images import *
from Player import Player
from OpponentOne import OpponentOne
from OpponentTwo import OpponentTwo
from View import View
from Game import Game

"""
File contains main function of the game.
"""


def main():
    """
    Function that starts the game.
    """

    player = Player()
    opponents_one_list = [OpponentOne(), OpponentOne(), OpponentOne(), OpponentOne(), OpponentOne()]
    opponents_two_list = [OpponentTwo(), OpponentTwo(), OpponentTwo(), OpponentTwo(), OpponentTwo()]
    view = View()
    screen = view.screen
    clock = pygame.time.Clock()
    game = Game()
    game.game_loop(clock=clock, view=view, player=player, opponents_one_list=opponents_one_list,
                   opponents_two_list=opponents_two_list, screen=screen)


main()

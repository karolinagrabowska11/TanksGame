import pygame

"""
File contains all constants for the game.
"""

PICTURE_EDGE = 32

UP = (0, -PICTURE_EDGE)
DOWN = (0, PICTURE_EDGE)
RIGHT = (PICTURE_EDGE, 0)
LEFT = (-PICTURE_EDGE, 0)

DIRECTIONS = {'UP': (0, -PICTURE_EDGE), 'DOWN': (0, PICTURE_EDGE),
              'RIGHT': (PICTURE_EDGE, 0), 'LEFT': (-PICTURE_EDGE, 0)}

DIRECTIONS_KEYS = ['UP', 'DOWN', 'RIGHT', 'LEFT']

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(0, 0, 255)
LIGHT_BLUE = pygame.Color(179, 204, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
LIGHT_GREEN = pygame.Color(128, 255, 212)
YELLOW = pygame.Color(255, 255, 0)

map_level_1 = """
   b     bgg 
 bbb  w    g 
             
  w  bbbbb b 
w w  b w b ww
w gggbwwwb   
     b w b   
     bw wb  g
 w   b   b  g
w    bbbbb   
          www
bbw w     www
 b        www"""

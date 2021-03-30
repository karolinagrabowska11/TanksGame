import pygame

"""
File contains all images for the game.
"""

wall_image = pygame.image.load('Tanks_Pack/w.png')
brick_image = pygame.image.load('Tanks_Pack/b.png')
grass_image = pygame.image.load('Tanks_Pack/g.png')

player_up_image = pygame.image.load('Tanks_Pack/player_up.png')
player_down_image = pygame.image.load('Tanks_Pack/player_down.png')
player_right_image = pygame.image.load('Tanks_Pack/player_right.png')
player_left_image = pygame.image.load('Tanks_Pack/player_left.png')

opponent_1_up_image = pygame.image.load('Tanks_Pack/opponent1_up.png')
opponent_1_down_image = pygame.image.load('Tanks_Pack/opponent1_down.png')
opponent_1_right_image = pygame.image.load('Tanks_Pack/opponent1_right.png')
opponent_1_left_image = pygame.image.load('Tanks_Pack/opponent1_left.png')

opponent_2_up_image = pygame.image.load('Tanks_Pack/opponent2_up.png')
opponent_2_down_image = pygame.image.load('Tanks_Pack/opponent2_down.png')
opponent_2_right_image = pygame.image.load('Tanks_Pack/opponent2_right.png')
opponent_2_left_image = pygame.image.load('Tanks_Pack/opponent2_left.png')

shot_up_image = pygame.image.load('Tanks_Pack/plasma_up.png')
shot_down_image = pygame.image.load('Tanks_Pack/plasma_down.png')
shot_right_image = pygame.image.load('Tanks_Pack/plasma_right.png')
shot_left_image = pygame.image.load('Tanks_Pack/plasma_left.png')

flash_up_image = pygame.image.load('Tanks_Pack/flash_up.png')
flash_down_image = pygame.image.load('Tanks_Pack/flash_down.png')
flash_right_image = pygame.image.load('Tanks_Pack/flash_right.png')
flash_left_image = pygame.image.load('Tanks_Pack/flash_left.png')
flash_img_dict = {'UP': flash_up_image,
                  'DOWN': flash_down_image,
                  'RIGHT': flash_right_image,
                  'LEFT': flash_left_image}

smoke_up_image = pygame.image.load('Tanks_Pack/smoke_up.png')
smoke_down_image = pygame.image.load('Tanks_Pack/smoke_down.png')
smoke_right_image = pygame.image.load('Tanks_Pack/smoke_right.png')
smoke_left_image = pygame.image.load('Tanks_Pack/smoke_left.png')
smoke_img_dict = {'UP': smoke_up_image,
                  'DOWN': smoke_down_image,
                  'RIGHT': smoke_right_image,
                  'LEFT': smoke_left_image}

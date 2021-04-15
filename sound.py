import pygame

pygame.mixer.init()
shot_sound = pygame.mixer.Sound('Tanks_Pack/shot.wav')
opponent_shot_sound = pygame.mixer.Sound('Tanks_Pack/opponent_shot_sound.flac')
brick_destroy_sound = pygame.mixer.Sound('Tanks_Pack/brick_destroy.wav')
impact = pygame.mixer.Sound('Tanks_Pack/impact.wav')

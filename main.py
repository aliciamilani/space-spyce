import pygame
from rank_screen import *
from main_menu import *

pygame.init()

screen_resolution = (1000, 500)

screen = pygame.display.set_mode(screen_resolution)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    #make_screen_rank(screen)
    main_menu()
    pygame.display.flip()

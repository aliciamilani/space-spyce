import pygame
from main_menu import *
from rank_screen import make_screen_rank
from testes_inimigo_2 import *

pygame.init()
clock = pygame.time.Clock()

screen_resolution = (1000, 500)

screen = pygame.display.set_mode(screen_resolution)

ovnis = []
ovnis.append(make_ovni())
ovni_sprite = pygame.image.load("content/nave_teste.png")

while True:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    main_menu()
    make_screen_rank(screen)
    update_ovni(screen, ovni_sprite, ovnis)
    pygame.display.flip()

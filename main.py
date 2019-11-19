import pygame
import menu
import rank
from enemy_2 import update_ovni, make_ovni
import controls
import credits

global screen_width
global screen_height

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# ovnis = []
# ovnis.append(make_ovni())
# ovni_sprite = pygame.image.load("content/nave_teste.png")

# declaração de variaveis de controle
run = True  # execução do jogo
init = True  # tela inicial
ranking = False
cred = False
game = False  # gameplay


while run:

    # tela inicial
    if init:
        decision = menu.make_screen_menu(screen, screen_width)
    
    # tela de rank
    if ranking:
        rank.make_screen_rank(screen)

    # tela de creditos
    if cred:
        credits.make_screen_credits(screen)

    # gameplay
    # if game:
    #     make_screen_game(screen)
    
    # checagem dos eventos acima
    for event in pygame.event.get():
        run = controls.close(event, run)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                decision = "null"
                ranking = False
                init = True
                cred = False
                game = False 
    
    if decision == 'rank':
        ranking = True
        init = False
        cred = False
        game = False
    
    elif decision == 'credits':
        ranking = False
        init = False
        cred = True
        game = False

    elif decision == 'start':
        ranking = False
        init = False
        cred = False
        game = True
    
    elif decision == 'exit':
        pygame.quit()

    # update_ovni(screen, ovni_sprite, ovnis)

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

 
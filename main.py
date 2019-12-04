import pygame
import menu
import credits
import gameplay
global screen_width
global screen_height

pygame.init()
pygame.display.set_caption("SPACE S.pyCE")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# declaração de variaveis de controle
run = True  # execução do jogo
init = True  # tela inicial
cred = False
game = False  # gameplay

while run:

    # tela inicial
    if init:
        decision = menu.make_screen_menu(screen, screen_width)

    # tela de creditos
    if cred:
        credits.make_screen_credits(screen)

    # gameplay
    if game:
        gameplay.make_screen_game(screen)
        decision = "null"
        game = cred = False
        init = True

    # checagem dos eventos acima
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                decision = "null"
                game = cred = False
                init = True


    if decision == 'credits':
        game = init = False
        cred = True

    elif decision == 'start':
        init = cred = False
        game = True

    elif decision == 'exit':
        pygame.quit()

    pygame.display.flip()
    clock.tick(30)
    pygame.display.update()

import pygame
import player
from enemy_2 import update_ovni, make_ovni

pygame.init()


def make_screen_game(screen):
    x_nave = 30
    y_nave = 200

    background = "nebula.jpg"
    pygame.display.set_caption("Gameplay")
    bg = pygame.image.load("content/{}".format(background))
    game = True
    while game:
        screen.blit(bg, (0, 0))
        player.draw_nave(screen, x_nave, y_nave)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_nave -= 10
                if event.key == pygame.K_DOWN:
                    y_nave += 10

        ovnis = []
        ovnis.append(make_ovni())
        ovni_sprite = pygame.image.load("content/nave_teste.png")

        update_ovni(screen, ovni_sprite, ovnis)

        pygame.display.flip()
        pygame.display.update()
        

        
        




import pygame
import random
import support
import enemy_2
pygame.init()


def make_screen_game(screen):
    x_nave = 30
    y_nave = 200
    ovni_sprite = pygame.image.load("content/nave_teste.png")
    shot_ovni_sprite = pygame.image.load("content/bullet.png")
    x_bg = 0
    x_bg_2 = 0
    # shot_ovni_sprite = pygame.transform.rotate(shot_ovni_sprite, -180)
    background = "nebula.jpg"
    # bg_2 = pygame.image.load("content/stars.png")
    # pygame.display.set_caption("Gameplay")
    bg = pygame.image.load("content/{}".format(background))

    ovnis = []
    ovnis_shot = []
    spawn_chance = 0.04  # Chance de spawnar um ET

    shoot = []

    game = True

    while game:
        x_bg, x_bg_2 = support.bg_parallax(screen, bg, x_bg, x_bg_2,1994,2, -300)
        support.draw_nave(screen, x_nave, y_nave)

        if(random.random() < spawn_chance):
            ovnis.append(enemy_2.make_ovni(2))
        enemy_2.update_ovni(screen, ovni_sprite, ovnis, ovnis_shot, x_nave, y_nave)
        enemy_2.updade_shot(screen, shot_ovni_sprite, ovnis_shot, 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_nave -= 15
                if event.key == pygame.K_DOWN:
                    y_nave += 15
                if event.key == pygame.K_LEFT:
                    x_nave -= 15
                if event.key == pygame.K_RIGHT:
                    x_nave += 15
                if event.key == pygame.K_SPACE:
                    shoot.append(support.make_shot(3, x_nave, y_nave))

        support.update_shot(screen, shoot)
        pygame.display.flip()
        pygame.display.update()

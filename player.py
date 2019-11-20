import pygame
pygame.init()


def draw_nave(screen, x, y):
    nave_sprite = pygame.image.load("content/nave.png")
    nave_sprite = pygame.transform.rotate(nave_sprite, -45)

    screen.blit(nave_sprite, (x, y))
    return nave_sprite

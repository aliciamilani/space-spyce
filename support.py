import pygame
from random import randint, choice, random
pygame.init()


def draw_nave(screen, x, y):
    nave_sprite = pygame.image.load("content/nave.png")
    nave_sprite = pygame.transform.rotate(nave_sprite, -45)

    screen.blit(nave_sprite, (x, y))
    return nave_sprite


def make_shot(speed, x, y):
    vec = pygame.math.Vector2
    shot_info = {}
    shot_info['vec_init'] = vec(x, y)
    # shot_info['vec_mov'] = vec(((-1)-speed), randint(-2, 2)-(speed*random()))
    shot_info['vec_mov'] = vec(((-1)-speed), randint(-2, 2)-(speed*random()))

    shot_info['up'] = True
    return shot_info


def update_shot(screen, shoot_list):
    shoot_sprite = pygame.image.load("content/bullet.png")
    for shoot in shoot_list:
        if shoot['vec_init'].x < 10:
            shoot['up'] = False
        if(shoot['up']):
            shoot['vec_init'] += shoot['vec_mov']
            if(shoot['vec_init'].y < 10 or shoot['vec_init'].y > 450):
                shoot['vec_mov'].y *= -1
            screen.blit(shoot_sprite, shoot['vec_init'])
        else:
            shoot_list.remove(shoot)

import pygame
from random import randint, choice, random


def make_ovni(speed = 1):
    vec = pygame.math.Vector2
    ovni_info = {}
    ovni_info['vec_init'] = vec(1020, randint(0, 500))
    ovni_info['vec_mov'] = vec(((-1)-speed), randint(-2,2)-(speed*random()))
    ovni_info['up'] = True
    return ovni_info


def update_ovni(screen, sprite, ovni_list):
    for ovni in ovni_list:
        if ovni['vec_init'].x < 10:
            ovni['up'] = False
        if(ovni['up']):
            ovni['vec_init'] += ovni['vec_mov']
            if(ovni['vec_init'].y < 100 or ovni['vec_init'].y > 450):
                ovni['vec_mov'].y *= -1
            screen.blit(sprite, ovni['vec_init'])
        else:
            ovni_list.remove(ovni)

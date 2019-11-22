import pygame
from random import randint, choice, random


def make_ovni(speed=1):
    vec = pygame.math.Vector2
    ovni_info = {}
    ovni_info['vec_init'] = vec(1020, randint(0, 500))
    ovni_info['vec_mov'] = vec(((-1)-speed), randint(-2, 2)-(speed*random()))
    ovni_info['up'] = True
    return ovni_info


def make_shot(begin, end):
    vec = pygame.math.Vector2
    shot_info = {}
    shot_info['vec_init'] = begin
    shot_info['vec_mov'] = vec.normalize((end - begin))
    shot_info['up'] = True
    return shot_info


def updade_shot(screen, sprite, shot_list, speed):
    for shot in shot_list:
        if shot['vec_init'].x < 10:
            shot['up'] = False
        if shot['up']:
            shot['vec_init'] += shot['vec_mov']*speed
            screen.blit(sprite, shot['vec_init'])
        else:
            shot_list.remove(shot)


def update_ovni(screen, sprite, ovni_list, shot_list, x_nave, y_nave):
    vec = pygame.math.Vector2
    for ovni in ovni_list:
        if ovni['vec_init'].x < 10:
            ovni['up'] = False

        if(ovni['up']):
            ovni['vec_init'] += ovni['vec_mov']
            if(ovni['vec_init'].y < 10 or ovni['vec_init'].y > 450):
                ovni['vec_mov'].y *= -1
            screen.blit(sprite, ovni['vec_init'])

            if(random() < 0.001):
                begin = vec(ovni['vec_init'].x, ovni['vec_init'].y)
                shot_list.append(make_shot(begin, vec(x_nave, y_nave)))

        else:
            ovni_list.remove(ovni)

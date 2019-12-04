import pygame
from random import randint, choice, random
 

def make_rock(speed=2):
    vec = pygame.math.Vector2
    rock_info = {}
    rock_info['vec_init'] = vec(randint(1000, 1300), randint(0, 500))
    rock_info['vec_mov'] = vec(randint(-speed*2, speed*2))
    rock_info['up'] = True
    return rock_info


def make_ovni(speed=1):
    vec = pygame.math.Vector2
    ovni_info = {}
    ovni_info['vec_init'] = vec(1020, randint(15, 450))
    ovni_info['vec_mov'] = vec(randint(-speed*2, -1), randint(-speed, speed))
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


def update_ovni(screen, sprite, ovni_list, shot_list, shot_chance, x_nave, y_nave):
    vec = pygame.math.Vector2
    for ovni in ovni_list:
        if ovni['vec_init'].x < -40:
            ovni['up'] = False

        if(ovni['up']):
            ovni['vec_init'] += ovni['vec_mov']
            if(ovni['vec_init'].y < 10 or ovni['vec_init'].y > 500):
                ovni['vec_mov'].y *= -1
            screen.blit(sprite, ovni['vec_init'])

            if(random() < shot_chance):
                begin = vec(ovni['vec_init'].x, ovni['vec_init'].y)
                shot_list.append(make_shot(begin, vec(x_nave, y_nave)))

        else:
            ovni_list.remove(ovni)


def update_rock(screen, sprite, rock_list, spawn_chance_rock):
    vec = pygame.math.Vector2
    for rock in rock_list:
        if rock['vec_init'].x < -40:
            rock['up'] = False
        if(rock['up']):
            rock['vec_init'] += rock['vec_mov']
            if(rock['vec_init'].y < 10 or rock['vec_init'].y > 450):
                rock['vec_mov'].y *= -1
            screen.blit(sprite, rock['vec_init'])
        else:
            rock_list.remove(rock)
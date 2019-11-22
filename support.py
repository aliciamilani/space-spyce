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
    shot_info['vec_init'] = vec(x+85, y+33)
    shot_info['vec_mov'] = vec(speed, 0)

    shot_info['up'] = True
    return shot_info


def update_shot(screen, shoot_list):
    shoot_sprite = pygame.image.load("content/bullet.png")
    for shoot in shoot_list:
        if shoot['vec_init'].x > 1000:
            shoot['up'] = False

        if(shoot['up']):
            shoot['vec_init'] += shoot['vec_mov']
            screen.blit(shoot_sprite, shoot['vec_init'])

        else:
            shoot_list.remove(shoot)


def bg_parallax(screen, bg, x_bg, x_bg_2, bg_width, speed, y):
    if(x_bg <= 0):
        x_bg_2 = bg_width - abs(x_bg)
    else:
        x_bg_2 -= speed
    screen.blit(bg, (x_bg, y))
    screen.blit(bg, (x_bg_2, y))
    if(x_bg <= -bg_width):
        x_bg = bg_width
    x_bg -= speed
    return x_bg, x_bg_2

def colide_with_nave(x_nave, y_nave, width_nave, height_nave, list_object, width_object, height_object):
    nave_rect = pygame.Rect(x_nave, y_nave, width_nave, height_nave)
    cont_colides = 0
    for thing in list_object:
        object_rect = pygame.Rect(thing['vec_init'].x, thing['vec_init'].y, width_object, height_object)
        if object_rect.colliderect(nave_rect):
            cont_colides += 1
            list_object.remove(thing)
    return cont_colides
import pygame
from random import randint, choice, random
pygame.init()


def draw_nave(screen, x, y):
    nave_sprite = pygame.image.load("content/nave.png")
    nave_sprite = pygame.transform.rotate(nave_sprite, -45)
    screen.blit(nave_sprite, (x, y))
    return nave_sprite


def check_pos_nave(x_nave, y_nave):
    if y_nave < -10:
        y_nave += 5
    elif y_nave > 435:
        y_nave -= 5

    if x_nave < 0:
        x_nave += 5
    elif x_nave > 910:
        x_nave -= 5

    return x_nave, y_nave


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


def colide_with_nave(x_nave, y_nave, width_nave, height_nave,
                     list_object, width_object, height_object):
    nave_rect = pygame.Rect(x_nave, y_nave, width_nave, height_nave)
    cont_colides = 0
    for thing in list_object:
        object_rect = pygame.Rect(thing['vec_init'].x, thing['vec_init'].y,
                                  width_object, height_object)
        if object_rect.colliderect(nave_rect):
            cont_colides += 1
            list_object.remove(thing)
    return cont_colides


def colide_shot_shot(list_shots_nave, list_shots_ovni, width_shot, height_shot):
    for shot_nave in list_shots_nave:
        rect_shot_nave = pygame.Rect(shot_nave['vec_init'].x, shot_nave['vec_init'].y,
                                     width_shot, height_shot)
        for shot_ovni in list_shots_ovni:
            rect_shot_ovni = pygame.Rect(shot_ovni['vec_init'].x, shot_ovni['vec_init'].y,
                                         width_shot, height_shot)
            if rect_shot_nave.colliderect(rect_shot_ovni):
                list_shots_ovni.remove(shot_ovni)
                list_shots_nave.remove(shot_nave)


def colide_shot_enemy(list_shots_nave, list_enemys, width_shot, height_shot, width_enemy, height_enemy):
    for shot_nave in list_shots_nave:
        rect_shot_nave = pygame.Rect(shot_nave['vec_init'].x, shot_nave['vec_init'].y,
                                     width_shot, height_shot)
        for enemy in list_enemys:
            rect_enemy = pygame.Rect(enemy['vec_init'].x, enemy['vec_init'].y,
                                     width_enemy, height_enemy)
            if rect_shot_nave.colliderect(rect_enemy):
                list_shots_nave.remove(shot_nave)
                list_enemys.remove(enemy)

def make_life_up(speed=3):
    vec = pygame.math.Vector2
    power_up_info = {}
    power_up_info['vec_init'] = vec(1020, randint(10, 450))
    power_up_info['vec_mov'] = vec((randint(0, 100)%speed),(randint(0, 100)%speed))
    power_up_info['up'] = True
    return power_up_info

def power_colides_nave(power_width, power_height, x_power, y_power, nave_width, nave_heigth, x_nave, y_nave):
    power_rect = pygame.Rect(x_power, y_power, power_width, power_height)
    nave_rect = pygame.Rect(x_nave, y_nave, nave_width, nave_heigth)
    if power_rect.colliderect(nave_rect):
        return True
    return False

def update_life_up(screen, sprite, list_life_up, x_nave, y_nave):
    vec = pygame.math.Vector2
    for life in list_life_up:
        if life['up']:
            screen.blit(sprite, life['vec_init'])
            life['vec_init'] -= life['vec_mov']
            if power_colides_nave(24, 24, life['vec_init'].x, life['vec_init'].y, 64, 64, x_nave, y_nave):
                list_life_up.remove(life)
                return True
            if life['vec_init'].x < -10:
                life['up'] = False
            if life['vec_init'].y < 0 or life['vec_init'].y > 500:
                life['vec_mov'].y *= -1
        else:
            list_life_up.remove(life)
            return False
    return False

def colide_rock_nave(screen, sprite_rock, rock_list, rock_width, rock_height, 
                        x_nave, y_nave, nave_width, nave_height):
    nave_rect = pygame.Rect(x_nave, y_nave, nave_width, nave_height)
    for rock in rock_list:
        rock_rect = pygame.Rect(rock['vec_init'].x, rock['vec_init'].y,
                                  rock_width, rock_height)
        if rock_rect.colliderect(nave_rect):
            rock_list.remove(rock)
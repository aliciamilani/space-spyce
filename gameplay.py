import pygame
import random
import support
import enemy_2
import hud
import menu
pygame.init()


def make_screen_game(screen):
    speed_init_para = 3
    global x_nave
    global y_nave
    global init
    x_nave = 50
    y_nave = 200

    ovni_sprite = pygame.image.load("content/new_sprites/enemie.png")
    ovni_sprite = pygame.transform.rotate(ovni_sprite, -90)
    ovni_sprite = pygame.transform.scale(ovni_sprite, (60,80))


    shot_ovni_sprite = pygame.image.load("content/new_sprites/enemie_laser.png")
    shot_ovni_sprite = pygame.transform.scale(shot_ovni_sprite, (20,20))

    power_up_sprite = pygame.image.load("content/new_sprites/pill_red.png")
    rock_sprite = pygame.image.load("content/pedra.png")
    
    x_bg = 0
    x_bg_2 = 0
    life = 3
    score = 0
    background = "nebula.jpg"
    bg = pygame.image.load("content/{}".format(background))

    list_power_up = []
    ovnis = []
    ovnis_shot = []
    rocks = []
    shoot = []
    spawn_chance_et = 0.01  # Chance de spawnar um ET
    spawn_chance_life = 0.001 # Chance de spawnar um power up
    spawn_chance_rock = 0.004 # Chance de spawnar uma pedra

    gameplay = True
    y_nave_up = False
    y_nave_down = False
    x_nave_left = False
    x_nave_right = False

    while gameplay:

        speed_para = score//500 + speed_init_para
        x_nave, y_nave = support.check_pos_nave(x_nave, y_nave)

        x_bg, x_bg_2 = support.bg_parallax(screen, bg, x_bg,
                                           x_bg_2, 1994, speed_para, -300)
        
        support.draw_nave(screen, x_nave, y_nave)

        if(random.random() < spawn_chance_et):
            ovnis.append(enemy_2.make_ovni(2))
        if(random.random() < spawn_chance_life):
            list_power_up.append(support.make_life_up(10))
        if(random.random() < spawn_chance_rock):
            rocks.append(enemy_2.make_rock(2))

        power_up = support.update_life_up(screen, power_up_sprite, list_power_up, x_nave, y_nave)

        if power_up:
            life += 1
            life = min(life,4)

        enemy_2.update_ovni(screen, ovni_sprite, ovnis,
                            ovnis_shot, 0.001,x_nave, y_nave)
        enemy_2.updade_shot(screen, shot_ovni_sprite, ovnis_shot, 2)
        enemy_2.update_rock(screen, rock_sprite, rocks, spawn_chance_rock)

        damage_taken = support.colide_with_nave(x_nave, y_nave,
                                                60, 80, ovnis_shot, 20, 20)

        damage_taken += support.colide_with_nave(x_nave, y_nave,
                                                 60, 80, ovnis, 60, 80)
         
        damage_taken += support.colide_rock_nave(screen, rock_sprite, rocks, 40, 40, x_nave, y_nave, 60, 80)
        
        support.colide_shot_shot(shoot, ovnis_shot, 12, 30, 20, 20)
        score += support.colide_shot_enemy(shoot, ovnis, 12, 30, 60, 80)
        score += support.colide_shot_rock(shoot, rocks, 12, 30, 40, 40)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_nave_up = True
                if event.key == pygame.K_DOWN:
                    y_nave_down = True
                if event.key == pygame.K_LEFT:
                    x_nave_left = True
                if event.key == pygame.K_RIGHT:
                    x_nave_right = True
                if event.key == pygame.K_SPACE:
                    shoot.append(support.make_shot(3, x_nave, y_nave))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_nave_up = False
                if event.key == pygame.K_DOWN:
                    y_nave_down = False
                if event.key == pygame.K_LEFT:
                    x_nave_left = False
                if event.key == pygame.K_RIGHT:
                    x_nave_right = False

        if y_nave_up:
            y_nave -= 2
        if y_nave_down:
            y_nave += 2
        if x_nave_left:
            x_nave -= 2
        if x_nave_right:
            x_nave += 2
        
        if life <= 0:
            decision = menu.make_gameover(screen, 1000)
            if decision:
                pygame.quit()
            else:
                global game
                gameplay = False
                init = True
                game = False

        life -= damage_taken
        hud.show_hud(screen, life, score)

        support.update_shot(screen, shoot, 10)
        pygame.display.flip()
        pygame.display.update()

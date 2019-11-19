import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
font = "content/UbuntuMono-R.ttf"
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
clock = pygame.time.Clock()

def format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText

def main_menu():
 
    menu = True
    selected = "start"
 
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected = "start"
                if event.key == pygame.K_2:
                    selected = "rank"
                if event.key == pygame.K_3:
                    selected = "credits"
                if event.key == pygame.K_4:
                    selected = "exit"
 
        bg = pygame.image.load('content/nebula.jpg')
        screen.blit(bg, (0,0))
        title = format("JOGO SEM NOME", font, 90, red)
        
        if selected == "start":
            start = format("START", font, 75, red)
        else:
            start = format("START", font, 75, white)

        if selected == "rank":
            rank = format("RANK", font, 75, red)
        else:
            rank = format("RANK", font, 75, white)

        if selected == "credits":
           credit = format("CREDITS", font, 75, red)
        else:
            credit = format ("CREDITS", font, 75, white)
 
        if selected == "exit":
            quitt = format("EXIT", font, 75, red)
        else:
            quitt = format("EXIT", font, 75, white)
        disc = format("utilize os números de 1 a 4 para escolher a sua opção", font, 14, white)
        
        disc_col = disc.get_rect()
        title_col = title.get_rect()
        start_col = start.get_rect()
        rank_col = rank.get_rect()
        credits_col = credit.get_rect()
        quit_col = quitt.get_rect()
        
        screen.blit(title, (screen_width/2 - (title_col[2]/2), 10))
        screen.blit(disc, (screen_width/2 - (disc_col[2]/2), 100))
        screen.blit(start, (screen_width/2 - (start_col[2]/2), 200))
        screen.blit(rank, (screen_width/2 - (rank_col[2]/2), 250))
        screen.blit(credit, (screen_width/2 - (credits_col[2]/2), 300))
        screen.blit(quitt, (screen_width/2 - (quit_col[2]/2), 350))
        pygame.display.update()
        clock.tick(30)
        pygame.display.set_caption("MENU")
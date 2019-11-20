import pygame
from pygame.locals import *
pygame.init()


font = "content/UbuntuMono-R.ttf"
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
clock = pygame.time.Clock()

def format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


def make_screen_menu(screen, screen_width):
    list_menu = ['start', 'rank', 'credits', 'exit']
    menu = True
    selected = 0

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected -= 1
                if event.key == pygame.K_DOWN:
                    selected += 1
                if event.key == pygame.K_RETURN:
                    return list_menu[selected]

        selected %= 4

        bg = pygame.image.load('content/nebula.jpg')
        screen.blit(bg, (0,0))
        title = format("JOGO SEM NOME", font, 90, red)

        start = format("START", font, 75, white)
        rank = format("RANK", font, 75, white)
        credit = format ("CREDITS", font, 75, white)
        quitt = format("EXIT", font, 75, white)
        
        if selected == 0:
            start = format("START", font, 75, red)

        elif selected == 1:
            rank = format("RANK", font, 75, red)

        elif selected == 2:
            credit = format("CREDITS", font, 75, red)
 
        elif selected == 3:
            quitt = format("EXIT", font, 75, red)

        disc = format("Use as setas para movimentar", font, 14, white)
        
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

        
        pygame.display.set_caption("MENU")

        pygame.display.update()
        clock.tick(30)
        
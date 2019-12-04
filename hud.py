import pygame
from random import choice
pygame.init()

font = "content/Righteous-Regular.ttf"

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (153, 51, 255)
pink = (255, 0, 127)
grey = (192, 192, 192)
pink2 = (255, 0, 255)


list_colors = [pink, red, yellow, green, blue, white, orange, purple, pink2, grey]

def format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText

def show_hud(screen, lifes, score):
    text_life = format('Lifes : {}'.format(lifes), font, 30, list_colors[lifes])
    screen.blit(text_life, (15, 15))
    text_score = format('Score : {}'. format(score), font, 30, choice(list_colors))
    screen.blit(text_score, (400, 15))





import pygame
from pygame import event
import menu


def close(event, run):  # evento para fechar o jogo
    if event.type == pygame.QUIT:
        run = False
    return run

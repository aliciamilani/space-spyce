import pygame
import ast

pygame.init()


def ranking(text_tam, text_font, rank_arq, text_color):
    # função para ler o arquivo
    arq = open("content/{}".format(rank_arq)).readline()
    dic_rank = ast.literal_eval(arq)
    cont = len(dic_rank)
    list_ranking = []
    font = pygame.font.SysFont(text_font, text_tam)
    if cont:
        for player in sorted(dic_rank, key=dic_rank.get):
            text = font.render("{}. {} - {} points".format(cont, player,
                               dic_rank[player]), True, text_color)
            list_ranking.append(text)
            cont -= 1
    return list_ranking


def write_rank(screen, text_tam, text_font, rank_arq, text_color):
    list_texts = ranking(text_tam, text_font, rank_arq, text_color)
    x_init = 320
    y_init = 20
    for text in list_texts[::-1]:
        screen.blit(text, (x_init, y_init))
        y_init += text.get_height() + 10


def make_screen_rank(screen, text_font="ubuntumono", text_tam=34,
                     background="nebula.jpg", text_color=(255, 255, 255),
                     rank_arq="rank.txt"):
    pygame.display.set_caption("Rank")
    bg = pygame.image.load("content/{}".format(background))
    screen.blit(bg, (0, 0))
    write_rank(screen, text_tam, text_font, rank_arq, text_color)

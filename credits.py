import pygame
import ast
  
pygame.init()


def crediting(text_tam, text_font, cred_arq, text_color):
    # função para ler o arquivo

    list_texts = []
    arq = open(cred_arq, 'r')
    for line in arq:
        list_texts.append(line)
    arq.close()

    list_cred = []
    font = pygame.font.SysFont(text_font, text_tam)

    for cred in list_texts:
        text = font.render(cred, True, text_color)
        list_cred.append(text)

    return list_cred


def write_credits(screen, text_tam, text_font, cred_arq, text_color):
    list_texts = crediting(text_tam, text_font, cred_arq, text_color)
    x_init = 300
    y_init = 20
    for text in list_texts:
        screen.blit(text, (x_init, y_init))
        y_init += text.get_height() + 10


def make_screen_credits(screen, text_font="ubuntumono", text_tam=20,
                        background="nebula.jpg", text_color=(255, 255, 255),
                        cred_arq="content/credits.txt"):
    pygame.display.set_caption("Créditos")
    bg = pygame.image.load("content/{}".format(background))
    screen.blit(bg, (0, 0))
    write_credits(screen, text_tam, text_font, cred_arq, text_color)

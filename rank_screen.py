import pygame
import ast

pygame.init()

# função para ler o arquivo
def ranking(font_tam):
    arq = open("content/rank.txt").readline()
    dic_rank = ast.literal_eval(arq)
    cont = len(dic_rank)
    list_ranking = []
    font = pygame.font.SysFont("ubuntumono", font_tam)
    if cont:
        for player in sorted(dic_rank, key = dic_rank.get):
            text = font.render("{}. {} - {} points".format(cont, player,
                                                           dic_rank[player]), True, (255, 255, 250))
            list_ranking.append(text)
            cont-=1
    return list_ranking

def write_rank():
    global screen
    list_texts = ranking(40)
    x_init = 250
    y_init = 0
    for text in list_texts[::-1]:
        screen.blit(text, (x_init, y_init))
        y_init += text.get_height() + 10

screen_resolution = (1000, 500)
clock_tick = 30

bg = pygame.image.load("content/nebula.jpg")

screen = pygame.display.set_mode(screen_resolution)

clock = pygame.time.Clock()

pygame.display.set_caption("Rank")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg, (0,0))
    write_rank()
    
    pygame.display.flip()
    clock.tick(clock_tick)
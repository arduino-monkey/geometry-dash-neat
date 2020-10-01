import pygame, sys, random

pygame.init()
pygame.font.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Geometry dash')
clock = pygame.time.Clock()

FONT = pygame.font.SysFont('comicsans', 40)

class PLayer:
    def __init__(self):
        pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(60)

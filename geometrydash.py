import pygame, sys, random

pygame.init()
pygame.font.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Geometry dash')
clock = pygame.time.Clock()

FONT = pygame.font.SysFont('comicsans', 40)

groundSurface = pygame.image.load('assets/ground.png')

class PLayer:
    def __init__(self):
        pass

x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if x <= -WIDTH:
        x = 0
    else:
        x -= 3
    
    screen.blit(groundSurface, (x, 50))
    screen.blit(groundSurface,(x + WIDTH, 50))
    pygame.display.update()
    clock.tick(60)

import pygame, sys, random

pygame.init()
pygame.font.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Geometry dash')
clock = pygame.time.Clock()

FONT = pygame.font.SysFont('comicsans', 40)


class Base:
    width = 1000
    height = 200
    rect = pygame.Rect(0,HEIGHT-height,width,height)
    def draw(self, screen):
        pygame.draw.rect(screen,(249, 1, 63),Base.rect)
    

def main():
    b = Base()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        b.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
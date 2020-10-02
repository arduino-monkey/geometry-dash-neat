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
    height = 100
    y = HEIGHT-height
    color = (249, 1, 63)
    rect = pygame.Rect(0,y,width,height)
    def draw(self, screen):
        pygame.draw.rect(screen,Base.color,Base.rect)
    

class Player:
    surface = pygame.image.load('assets/player.png')
    x = 50
    gravity = 0.5
    def __init__(self, y):
        self.y = y
        self.rect = Player.surface.get_rect(bottomleft = (Player.x, self.y))
        self.movement = 0
        self.jumped = False
    def move(self):
        if self.rect.bottomleft[1] <= Base.y:
            self.movement += Player.gravity
            self.rect.centery += self.movement

    def draw(self, screen):
        screen.blit(Player.surface, self.rect)

    def jump(self):
        if self.rect.bottomleft[1] >= Base.y:
            self.movement = 0
            self.movement -= 10
            self.rect.centery += self.movement
        
class Enemy:
    surface = pygame.image.load('assets/enemy.png')
    y = Base.y
    vel = 3
    
    def __init__(self, x):
        self.x = x
        self.rect = Enemy.surface.get_rect(bottomleft=(self.y, Enemy.x))
    
    def move(self):
        self.x -= Enemy.vel
    
    def draw(self):
        screen.blit(Enemy.surface, self.rect)

def main():
    b = Base()
    p = Player(Base.y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.jump()
                
        screen.fill((0,0,0))
        p.move()
        b.draw(screen)
        p.draw(screen)
        pygame.display.flip()
        clock.tick(100)

if __name__ == '__main__':
    main()
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
    surface = pygame.image.load('assets/player.png').convert_alpha()
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
            self.movement -= 12
            self.rect.centery += self.movement

    def collide(self, enemy):
        collision = self.rect.colliderect(enemy.rect)
        if collision:
            return True
        else:
            return False
        
class Enemy:
    surface = pygame.image.load('assets/enemy.png').convert_alpha()
    y = Base.y
    vel = 5
    
    def __init__(self, x):
        self.x = x
        self.passed = False
        self.rect = Enemy.surface.get_rect(bottomleft=(self.x, Enemy.y))
    
    def move(self):
        self.x -= Enemy.vel
        self.rect.centerx -= Enemy.vel
    def draw(self, screen):
        screen.blit(Enemy.surface, self.rect)


def main():
    base = Base()
    player = Player(Base.y)
    enemies = [Enemy(1000)]
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                
        
        player.move()
        for enemy in enemies[:]:
            enemy.move()
            if player.collide(enemy):
                pygame.quit()
                sys.exit()
            if enemy.passed == False and enemy.x < 0:
                enemy.passed = True
                enemies.append(Enemy(1000))
                score += 1
                enemies.pop(0)
        
        
        screen.fill((255,255,255))
        base.draw(screen)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        scoreText = FONT.render(f'Score: {score}', 1, (0,0,0))
        screen.blit(scoreText, (0,0))   
        
        print(enemies)
        pygame.display.flip()
        clock.tick(100)


if __name__ == '__main__':
    main()
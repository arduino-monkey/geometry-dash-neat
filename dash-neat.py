import pygame, sys, random, neat, os

pygame.init()
pygame.font.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Geometry dash')

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
    #surface = pygame.image.load('assets/player.png').convert_alpha()
    gravity = 0.5
    def __init__(self, y):
        self.y = y-50
        self.x = random.randint(30,500)
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.movement = 0
    def move(self):
        if self.rect.bottomleft[1] <= Base.y:
            self.movement += Player.gravity
            self.y += self.movement
            self.rect.centery = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)

    def jump(self):
        if self.rect.bottomleft[1] >= Base.y:
            self.movement = 0
            self.movement -= 12
            self.y += self.movement
            self.rect.centery = self.y

    def collide(self, enemy):
        collision = self.rect.colliderect(enemy.rect)
        if collision:
            return True
        else:
            return False
        
class Enemy:
    surface = pygame.image.load('assets/enemy.png').convert_alpha()
    y = Base.y
    vel = 7
    
    def __init__(self, x):
        self.x = x
        self.passed = False
        self.rect = Enemy.surface.get_rect(bottomleft=(self.x, Enemy.y))
    
    def move(self):
        self.x -= Enemy.vel
        self.rect.centerx -= Enemy.vel
    def draw(self, screen):
        screen.blit(Enemy.surface, self.rect)


def main(genomes, config):
    nets = []
    players = []
    ge = []

    for genomeId, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        players.append(Player(Base.y))
        ge.append(genome)

    
    base = Base()
    enemies = [Enemy(1000)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while len(players) and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break

        enemyIndex = 0
        if len(players):
            if len(enemies) > 1 and 30 > enemies[0].x + 50:
                enemyIndex = 1 

        for i, player in enumerate(players):
            ge[i].fitness += 0.03
            player.move()
            dist = abs(player.x-enemies[-1].x)
            output = nets[i].activate((dist,))
            if output[0] >0.5:
                player.jump()
        
        rem = []
        addEnemy = False
        for enemy in enemies:
            enemy.move()
            for player in players:
                if player.collide(enemy):
                    playerIndex = players.index(player)
                    ge[playerIndex].fitness -= 1
                    nets.pop(playerIndex)
                    ge.pop(playerIndex)
                    players.pop(playerIndex)

            if enemy.x + 50 < 0:
                rem.append(enemy)
                
            if not enemy.passed and enemy.x < 30:
                enemy.passed = True
                addEnemy = True
        
        if addEnemy:
            score += 1
            for genome in ge:
                genome.fitness += 5
            enemies.append(Enemy(WIDTH))
        
        for r in rem:
            enemies.remove(r)


        screen.fill((255,255,255))
        base.draw(screen)

        for player in players:
            player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        
        scoreText = FONT.render(f'Score: {score}', 1, (0,0,0))
        screen.blit(scoreText, (0,0))   
        
        pygame.display.flip()
        clock.tick(100)

def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(main, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        
        screen.fill(color="black")
        
        updatables.update(dt)
        
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

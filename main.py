import pygame
from constants import *

def main():
    #Initialize
    pygame.init()
    
    #Set the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    n = False
    while n == False:
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    


if __name__ == "__main__":
    main()
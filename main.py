import pygame
from constants import *

def main():
    #Initialize
    pygame.init()
    
    #Set the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    


    print("Attempting to access constants...")
    print("Screen Width:", SCREEN_WIDTH)
    print("Screen Height:", SCREEN_HEIGHT)
    #Print Statements
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    n = False
    while n == False:
        screen.fill((0,0,0))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()
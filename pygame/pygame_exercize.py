"""fps_testl.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))

def main():
    """main routine"""
    sysfont = pygame.font.SysFont(None,36)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((0,0,0,))
        pygame.display.update()

if __name__=="__main__":
    main()

    

import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    """main routine"""
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,255))
        pygame.draw.line(SURFACE, (255, 0, 0), (10, 80), (200, 160), 10)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
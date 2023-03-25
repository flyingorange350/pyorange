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
        SURFACE.fill((255,255,255,))
        for xpos in range(0, 400, 25):
            pygame.draw.line(SURFACE, 0xFFFFFF, (xpos, 0), (xpos, 300))
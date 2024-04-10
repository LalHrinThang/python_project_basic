import pygame
import random
import math


pygame.init()

FPS = 60

WIDTH, HEIGHT = 800,800

ROWS = 4
COLS = 4

OUTLINE_COLOR = (187,17,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")


def draw(window):
    window.fill(BACKGROUND_COLOR)


    pygame.display.update()

def main(window): 
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window)
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)

FONT = pygame.font.SysFont("comicsans",60,bold=True)

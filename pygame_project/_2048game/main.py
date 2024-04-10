import pygame
import random
import math


pygame.init()

FPS = 60

WIDTH, HEIGHT = 800,800

ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187,170,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")

def draw_grid(window):

    for row in range(1,ROWS): # don't need to draw 4 horizontal line so it's started from 1
        y = row * RECT_HEIGHT
        pygame.draw.line(window,OUTLINE_COLOR,(0,y),(WIDTH,y),OUTLINE_THICKNESS)

    for col in range(1,COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window,OUTLINE_COLOR,(x,0),(x,HEIGHT),OUTLINE_THICKNESS)

    pygame.draw.rect(window,OUTLINE_COLOR,(0,0,WIDTH,HEIGHT),OUTLINE_THICKNESS) # 0,0 => start point coordinate / Width = height = 800 => end point coordinate 


def draw(window):
    window.fill(BACKGROUND_COLOR)

    draw_grid(window)

    pygame.display.update()

def main(window): 
    clock = pygame.time.Clock()
    run = True
     
# I want to run everycomputer to run the same speed as 60 FPS
    while run:
        clock.tick(FPS)


# exit_button click => exit from the game : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window)
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)

FONT = pygame.font.SysFont("comicsans",60,bold=True)

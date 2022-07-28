import pygame as pg
from pygame.locals import *

class Board:
    def __init__(self, screen, width, height, color):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pg.draw.rect(self.screen, self.color, (0, 0, self.width, self.height))

    def update(self):
        self.draw()

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Board")
    board = Board(screen, 800, 600, (0, 0, 0))
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
        screen.fill((255, 255, 255))
        board.update()
        pg.display.update()
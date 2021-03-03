background_image_filename = 'sushiplate.jpg'
SCREEN_SIZE = (640, 480)
message = "   This is a demonstration of the scrolly message script.   "

from sys import exit

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

font = pygame.font.SysFont("arial", 80);
text_surface = font.render(message, True, (0, 0, 255))

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2
SPACE = 0

background = pygame.image.load(background_image_filename).convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 2
    if x < -text_surface.get_width():
        x = 0

    # 前后两个字符串相互连接
    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width() + SPACE, y))

    pygame.display.update()

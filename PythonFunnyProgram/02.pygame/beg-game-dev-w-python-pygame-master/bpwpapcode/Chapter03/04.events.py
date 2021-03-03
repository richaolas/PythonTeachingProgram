from sys import exit

import pygame
from pygame.locals import *

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []

while True:

    event = pygame.event.wait()
    event_text.append(str(event))

    # 只取出最后 n 行文字
    event_text = event_text[-SCREEN_SIZE[1] // font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))

    # 从下到上，起始显示位置
    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        # 每显示一行，向上移动一行的高度
        y -= font_height

    pygame.display.update()

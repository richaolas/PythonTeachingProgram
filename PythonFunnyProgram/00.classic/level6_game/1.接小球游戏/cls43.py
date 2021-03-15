# -*- coding: utf-8 -*-
'''
pygame 显示文字
'''

import pygame

WIDTH = 600
HEIGHT = 500
R = 25
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game variable
life = 3
score = 0
padding = 10

# 初始化引擎
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# if using chinese
# lst = pygame.font.get_fonts()
# font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 25)

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y, color=(255,255,255), align=0):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == 0:  # left align
        text_rect.topleft = (x, y)
    elif align == 1:  # right align
        text_rect.topright = (x, y)
    elif align == 2:  # mid align
        text_rect.midtop = (x, y)

    surf.blit(text_surface, text_rect)


ball = pygame.Surface((2 * R, 2 * R))
ball.fill(BLACK)
ball.set_colorkey(BLACK)
pygame.draw.circle(ball, RED, (R, R), R)
ball = ball.convert()
rect = ball.get_rect()
rect.midtop = (WIDTH / 2, 0)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
    # 填充屏幕背景
    screen.fill((0, 0, 0))
    rect.y += 1
    screen.blit(ball, rect)
    # pygame.draw.circle(screen, (100, 100, 30), (100, 100), 30, 0)

    # 渲染文字
    draw_text(screen, "Life: {0}".format(life), 24, padding, padding, WHITE)
    draw_text(screen, "Score: {0}".format(score), 24, WIDTH - padding, padding, WHITE, 1)

    # 渲染屏幕
    pygame.display.update()

# 有能力同学完成事件在屏幕显示程序

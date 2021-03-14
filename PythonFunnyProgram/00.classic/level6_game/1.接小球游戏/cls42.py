'''
pygame 的基本使用
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

#初始化引擎
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = pygame.Surface((2*R, 2*R))
ball.fill(BLACK)
ball.set_colorkey(BLACK)
pygame.draw.circle(ball, RED, (R,R), R)
ball = ball.convert()
rect = ball.get_rect()
rect.midtop = (WIDTH/2, 0)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
    # 填充屏幕背景
    screen.fill((0,0,0))
    rect.y += 1
    screen.blit(ball, rect)
    # pygame.draw.circle(screen, (100, 100, 30), (100, 100), 30, 0)
    # 渲染屏幕
    pygame.display.update()

#有能力同学完成事件在屏幕显示程序
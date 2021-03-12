'''
pygame 的基本使用
'''

import pygame
#初始化引擎
pygame.init()

screen = pygame.display.set_mode((600, 500))

pos = [0, 100]

def update():
    pos[0] += 1

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
    # 填充屏幕背景
    screen.fill((0,0,0))
    update()
    pygame.draw.circle(screen, (100, 100, 30), pos, 30, 0)
    # 渲染屏幕
    pygame.display.update()

#有能力同学完成事件在屏幕显示程序
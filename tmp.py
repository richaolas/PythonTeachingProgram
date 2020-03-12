# -*- coding: utf-8 -*-
"""
__author__= 'Du'
__creation_time__= '2018/1/4 17:03'
"""

import sys
import pygame
from pygame.locals import *

import pygame
from pygame.locals import *

# WINDOW_W, WINDOW_H = 640, 480
# pygame.init()
# screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
# pygame.display.set_caption("小球弹跳")
# FPS = 60
# g = 9.8 * 100
# is_run = True  # 是否运行
# clock = pygame.time.Clock()
#
# x, y = WINDOW_W / 2, 10
# vx, vy = 0, 0
#
# def my_event():
#     global vx,vy,is_run
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#     if is_run:
#         vy += g * 1/FPS
#
# if __name__ == '__main__':
#     while True:
#         # 侦听事件
#         my_event()
#
#         # 是否暂停
#         if not is_run:
#             continue
#
#         # 计算小球
#         x += vx * 1 / FPS
#         y += vy * 1 / FPS
#         if y >= WINDOW_H - 10:
#             vy = -vy
#         if x >= WINDOW_W:
#             x-=WINDOW_W
#         if x < 0:
#             x+=WINDOW_W
#
#         # 将背景图画上去
#         screen.fill((0, 0, 0))
#         pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10)
#
#         # 刷新画面
#         pygame.display.update()
#         time_passed = clock.tick(FPS)


# def play_ball():
#     pygame.init()
#     # 窗口大小
#     window_size = (width, height) = (1000, 700)
#     # 小球运行偏移量[水平，垂直]，值越大，移动越快
#     speed = [2, 1]
#     # 窗口背景色RGB值
#     color_black = (50, 205, 0)
#     # 设置窗口模式
#     screen = pygame.display.set_mode(window_size)
#     # 设置窗口标题
#     pygame.display.set_caption('运动的小球')
#     # 加载小球图片
#     ball_image = pygame.image.load("test_circle.png")
#     # 获取小球图片的区域开状
#     ball_rect = ball_image.get_rect()
#
#     while True:
#         # 退出事件处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#         # 使小球移动，速度由speed变量控制
#         ball_rect = ball_rect.move(speed)
#
#         # 当小球运动出窗口时，重新设置偏移量
#         if (ball_rect.left < 0) or (ball_rect.right > width):
#             speed[0] = - speed[0]
#         if (ball_rect.top < 0) or (ball_rect.bottom > height):
#             speed[1] = - speed[1]
#
#         # 填充窗口背景  # 否则小球的运动轨迹会留下来
#         screen.fill(color_black)
#         # 在背景Surface上绘制 小球
#         screen.blit(ball_image, ball_rect)
#         # 更新窗口内容
#         pygame.display.update()
#
#
# if __name__ == '__main__':
#     play_ball()


import pygame
from pygame.locals import *

clock = pygame.time.Clock()
time_passed = clock.tick()
time_passed = clock.tick(30)

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('BALL')

ball_x = 0
ball_y = 100

backcolor = (0, 0, 0)
font1 = pygame.font.Font(None, 24)
def print_text(scr, font, x, y, text, color = (250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))

rect_x, rect_y, rect_w, rect_h = 20, 200, 50, 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(backcolor)
    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), 30, 0)
    ball_x += 1
    pygame.draw.rect(screen, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
    print_text(screen, font1, 200, 100, 'test')
    pygame.display.update()
    time_passed = clock.tick(30)


# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Pygame事件处理")
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.unicode == "":
#                 print("[KEYDOWN]:", "#", event.key, event.mod)
#             else:
#                 print("[KEYDOWN]:", event.unicode, event.key, event.mod)
#         elif event.type == pygame.MOUSEMOTION:
#             print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
#         elif event.type == pygame.MOUSEBUTTONUP:
#             print("[MOUSEBUTTONUP]:", event.pos, event.button)
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
#     pygame.display.update()

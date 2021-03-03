background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

from math import *
from sys import exit

import pygame
from pygame.locals import *
# from gameobjects.vector2 import Vector2
from pygame.math import *

'''
pygame.mouse.get_pressed()  ——  获取鼠标按键的情况（是否被按下）
pygame.mouse.get_pos()  ——  获取鼠标光标的位置
pygame.mouse.get_rel()  ——  获取鼠标一系列的活动
pygame.mouse.set_pos()  ——  设置鼠标光标的位置
pygame.mouse.set_visible()  ——  隐藏或显示鼠标光标
pygame.mouse.get_focused()  ——  检查程序界面是否获得鼠标焦点
pygame.mouse.set_cursor()  ——  设置鼠标光标在程序内的显示图像
pygame.mouse.get_cursor()  ——  获取鼠标光标在程序内的显示图像
'''

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
'''
如果鼠标光标被隐藏并且输入被当前显示器占用，鼠标会进入虚拟输入模式，在此模式内，鼠标的相关活动不会因为屏幕的边界限制而停止。
调用 pygame.mouse.set_visible() 方法和 pygame.event.set_grab()  方法进行设置。

note:这个时候鼠标被限制在窗口内了
'''
pygame.event.set_grab(True)

sprite_pos = Vector2(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.  # Degrees per second

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    '''
    获取鼠标一系列的活动。
    get_rel() -> (x, y)
    返回在调用此方法之前的一系列活动坐标 (x, y)。鼠标光标的相关活动被限制在屏幕范围内，但是通过虚拟输入模式可以突破这个限制。此页面的顶部有虚拟输入模式的描述。
    pygame.mouse.get_rel()返回的是鼠标距离上一次次在横纵轴方向的位移大小
    relative
    '''
    rotation_direction = pygame.mouse.get_rel()[0] / 5.0
    print(pygame.mouse.get_rel())

    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    if pressed_keys[K_UP] or pressed_mouse[0]:
        movement_direction = +1.
    if pressed_keys[K_DOWN] or pressed_mouse[2]:
        movement_direction = -1.

    screen.blit(background, (0, 0))

    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = sin(sprite_rotation * pi / 180.)
    heading_y = cos(sprite_rotation * pi / 180.)
    heading = Vector2(heading_x, heading_y)
    heading *= movement_direction

    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()

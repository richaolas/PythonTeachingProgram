
'''
Objects
'''

# put Python classes and functions here

'''
Setup
'''

# put run-once code here

'''
Main Loop
'''

# put game loop here

# the pygame template

# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 360
HEIGHT = 480
FPS = 30 # frame per second

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

role = pygame.image.load(os.path.join("res", "hero.png"))#.convert()
#role.set_colorkey(WHITE)
role_rect = role.get_rect()
# center the sprite on the screen
role_rect.center = (WIDTH / 2, HEIGHT / 2)

DIR_DOWN = 0
DIR_LEFT = 1
DIR_RIGHT = 2
DIR_UP = 3

direct = DIR_DOWN

frame = 0

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS) #隐藏fps来说明update原理
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            direct = DIR_UP
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            direct = DIR_DOWN
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            direct = DIR_LEFT
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            direct = DIR_RIGHT
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        #    role_rect.y += 5
            '''
            按键是默认只能按下一次，于是就取了一个巧，查看哪些按键是已进按下的，后通过循环实现对应操作
            key_pressed = pygame.key.get_pressed()
                if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]
                    plane_temp.move_left()
            '''
    # Update
    frame = (frame + 0.1) % 3

    # Draw / render
    screen.fill(BLACK) # 可以先隐藏fill来说明动画原理
    x = (int)(frame) * 32
    y = direct * 32
    screen.blit(role, (WIDTH / 2, HEIGHT / 2), (x, y, 32, 32))

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

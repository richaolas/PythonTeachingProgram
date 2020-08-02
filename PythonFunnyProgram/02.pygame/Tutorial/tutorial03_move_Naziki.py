
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

role_up = [
    pygame.image.load(os.path.join("res/Naziki", "Naziki_up_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_up_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_up_01.png"))]
role_down = [
    pygame.image.load(os.path.join("res/Naziki", "Naziki_down_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_down_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_down_01.png"))]
role_left = [
    pygame.image.load(os.path.join("res/Naziki", "Naziki_left_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_left_02.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_left_03.png"))]
role_right = [
    pygame.image.load(os.path.join("res/Naziki", "Naziki_right_01.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_right_02.png")),
    pygame.image.load(os.path.join("res/Naziki", "Naziki_right_03.png"))]

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

role = [role_up, role_down, role_left, role_right]
role_rect = role[0][0].get_rect()
# center the sprite on the screen
role_rect.center = (WIDTH // 2, HEIGHT // 2)

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

    '''
    按键是默认只能按下一次，于是就取了一个巧，查看哪些按键是已进按下的，后通过循环实现对应操作
    key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]
            plane_temp.move_left()
    '''
    speed = 5

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_SPACE]:
        speed *= 3
    # if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
    if key_pressed[pygame.K_s]:
        direct = DIR_DOWN
        role_rect.y += speed
        if role_rect.y > HEIGHT:
            role_rect.y = 0

    if key_pressed[pygame.K_w]:
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        direct = DIR_UP
        role_rect.y -= speed
        if role_rect.y < 0:
            role_rect.y = HEIGHT

    if key_pressed[pygame.K_d]:
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
        direct = DIR_RIGHT
        role_rect.x += speed
        if role_rect.x > WIDTH:
            role_rect.x = 0

    if key_pressed[pygame.K_a]:
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        direct = DIR_LEFT
        role_rect.x -= speed
        if role_rect.x < 0:
            role_rect.x = WIDTH

    # Update
    #cnt = len([x for x in key_pressed if x])
    if key_pressed[pygame.K_s] or key_pressed[pygame.K_w] or key_pressed[pygame.K_d] or key_pressed[pygame.K_a]:
        frame = (frame + 0.13) % 3

    # Draw / render
    screen.fill(BLACK) # 可以先隐藏fill来说明动画原理
    screen.blit(role[direct][int(frame)], role_rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

# 1. 直接设计屏幕尺寸大小，1‘ 利用缩放贴满尺寸
# 2. 通过小块贴图 for for 帖全屏
# 3. 利用大的图片作为地图
# 4. 利用两张图片进行轮换无尽贴图

################################################################
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
life = 3

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

slime_left = [
    pygame.image.load(os.path.join("res/slime", "slime_left_01.png")),
    pygame.image.load(os.path.join("res/slime", "slime_left_02.png")),
    pygame.image.load(os.path.join("res/slime", "slime_left_03.png"))]

slime = [slime_left]
slime_rect = slime[0][0].get_rect()
slime_rect.center = (WIDTH // 2 + 100, HEIGHT // 2)
slime_d = 0
slime_speed = 8
slime_frame = 0

heart = pygame.image.load(os.path.join("res/", "heart.png"))
heart_rect = heart.get_rect()

grass = pygame.image.load(os.path.join("res/", "grass.png"))
grass_rect = grass.get_rect()

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

    slime_frame = slime_frame + 1

    if slime_frame % 5== 0:
        slime_d = random.randint(0, 3)

    if slime_d == 0:
        slime_rect.y -= slime_speed
        if slime_rect.y < 0:
            slime_rect.y = 0

    if slime_d == 2:
        slime_rect.y += slime_speed
        if slime_rect.y + slime_rect.height > HEIGHT:
            slime_rect.y = HEIGHT - slime_rect.height

    if slime_d == 1:
        slime_rect.x += slime_speed
        if slime_rect.x + slime_rect.width > WIDTH:
            slime_rect.x = WIDTH - slime_rect.width

    if slime_d == 3:
        slime_rect.x -= slime_speed
        if slime_rect.x < 0:
            slime_rect.x = 0

    # Draw / render
    screen.fill(BLACK) # 可以先隐藏fill来说明动画原理

    for r in range(HEIGHT // grass_rect.height + 1):
        for c in range(WIDTH//grass_rect.width + 1):
            grass_rect.left = c * grass_rect.width
            grass_rect.top = r * grass_rect.height
            screen.blit(grass, grass_rect)

    for i in range(life):
        heart_rect.left = i * heart_rect.width + 10*i
        heart_rect.top = 10
        screen.blit(heart, heart_rect)

    # simple understand but not right
    #if slime_rect.top > role_rect.top and \
    #        slime_rect.top < role_rect.top + role_rect.height and \
    #    slime_rect.left > role_rect.left and \
    #        slime_rect.left < role_rect.left + role_rect.width:
    #    life = life - 1
    #    role_rect.left = role_rect.left - 100

    cross_l = max(slime_rect.x, role_rect.x)
    cross_t = max(slime_rect.y, role_rect.y)
    cross_r = min(slime_rect.x + slime_rect.width, role_rect.x + role_rect.width)
    cross_d = min(slime_rect.y + slime_rect.height, role_rect.y + role_rect.height)

    if cross_l < cross_r and cross_t < cross_d:
        life = life - 1
        next_loc = role_rect.left - (role_rect.width + slime_rect.width + 20)
        if next_loc < 0:
            next_loc = WIDTH - role_rect.width
        role_rect.left = next_loc

    screen.blit(role[direct][int(frame)], role_rect)
    screen.blit(slime[0][int(slime_frame/10.0%3)], slime_rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

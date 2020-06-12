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

block = pygame.Surface((50, 50))
block.fill(GREEN)
block_rect = block.get_rect()
# center the sprite on the screen
block_rect.center = (WIDTH / 2, HEIGHT / 2)

bgSurface1 = pygame.image.load('img_bg_level_1.jpg')
bgSurface1 = pygame.transform.scale(bgSurface1, (360, 480))
bgSurface1_rect = bgSurface1.get_rect()

bgSurface2 = pygame.image.load('img_bg_level_1.jpg')
bgSurface2 = pygame.transform.scale(bgSurface2, (360, 480))
bgSurface2_rect = bgSurface2.get_rect()
bgSurface2_rect.y = -bgSurface2_rect.height

#bgSurface = pygame.transform.scale(bgSurface, (360, 480))
#bgSurface = pygame.image.load('bmw.jpg')

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
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
        #     bgSurface_rect.y += 10
        #     #direct = DIR_UP
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        #     bgSurface_rect.y -= 10
            #direct = DIR_DOWN
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            #direct = DIR_LEFT
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            #direct = DIR_RIGHT

    # Update
    # block_rect.x += 5
    # if block_rect.x > WIDTH:
    #     block_rect.x = 0

    # Draw / render
    # screen.fill(BLACK) # 可以先隐藏fill来说明动画原理
    #screen.blit(block, block_rect)

    # for i in range(HEIGHT//32 + 1):
    #     for j in range(WIDTH//32 + 1):
    #         screen.blit(bgSurface, (j*32, i*32))

    bgSurface1_rect.y += 20
    bgSurface2_rect.y += 20

    if (bgSurface1_rect.y >= HEIGHT):
        bgSurface1_rect.y = 0#bgSurface2_rect.y - HEIGHT
    if (bgSurface2_rect.y >= HEIGHT):
        bgSurface2_rect.y = 0#bgSurface1_rect.y - HEIGHT

    screen.blit(bgSurface1, bgSurface1_rect)
    screen.blit(bgSurface2, bgSurface2_rect)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

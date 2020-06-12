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

    # Update
    block_rect.x += 5
    if block_rect.x > WIDTH:
        block_rect.x = 0

    # Draw / render
    screen.fill(BLACK) # 可以先隐藏fill来说明动画原理
    screen.blit(block, block_rect)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

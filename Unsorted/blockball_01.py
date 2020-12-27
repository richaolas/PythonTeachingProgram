
import pygame
import sys
import random

win_w, win_h = 600, 500
pygame.init()
screen = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('BALL')

ball_x, ball_y = 100, 100
ball_r = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    ball_x += 1
    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), ball_r, 0)
    pygame.display.update()
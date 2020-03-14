import pygame
import sys
import random

win_w, win_h = 600, 500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('BALLGAME')

ball_x, ball_y = 100, 500
ball_r = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))

    ball_y -= 10
    if ball_y < 0: #>= win_h-ball_r:
        ball_x=random.randint(ball_r, win_w - ball_r)
        ball_y = 500

    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), ball_r, 0)
    pygame.display.update()
    clock.tick(30)


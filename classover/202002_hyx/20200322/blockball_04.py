import pygame
import sys
import random

win_w, win_h = 600, 500
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('BALLGAME')

ball_x, ball_y = 100, 0
ball_r = 30

rect_w, rect_h = 120, 40
rect_x, rect_y = (win_w - rect_w) / 2, win_h - rect_h

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            if rect_w / 2 <= mouse_x <= win_w - rect_w / 2:
                rect_x = mouse_x - rect_w / 2
            elif mouse_x < rect_w / 2:
                rect_x = 0
            elif mouse_x > win_w - rect_w / 2:
                rect_x = win_w - rect_w

    screen.fill((255, 255, 255))

    ball_y += 10
    if ball_y >= win_h - ball_r:
        ball_x = random.randint(ball_r, win_w - ball_r)
        ball_y = 0

    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), ball_r, 0)
    pygame.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, rect_w, rect_h), 0)
    pygame.display.update()
    clock.tick(30)

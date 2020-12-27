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

score = 0

# 字体
font = pygame.font.Font(None, 60)

while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # 用鼠标控制挡板
            mouse_x, mouse_y = event.pos
            if rect_w / 2 <= mouse_x <= win_w - rect_w / 2:
                rect_x = mouse_x - rect_w / 2
            elif mouse_x < rect_w / 2:
                rect_x = 0
            elif mouse_x > win_w - rect_w / 2:
                rect_x = win_w - rect_w

    # 坐标调整
    # 判断碰撞得分
    if rect_x <= ball_x <= rect_x + rect_w and rect_y - ball_r <= ball_y:
        score += 1
        print(score)

        ball_x = random.randint(ball_r, win_w - ball_r)
        ball_y = 0

    # 控制小球落下
    ball_y += 10
    if ball_y >= win_h - ball_r:
        ball_x = random.randint(ball_r, win_w - ball_r)
        ball_y = 0

    # 绘制图形
    screen.fill((255, 255, 255))
    # 渲染 # 反锯齿
    textImage = font.render('SCORE: ' + str(score), True, (255, 0, 0))
    screen.blit(textImage, (100, 50))
    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), ball_r, 0)
    pygame.draw.rect(screen, (0, 0, 255), (rect_x, rect_y, rect_w, rect_h), 0)
    pygame.display.update()

    clock.tick(30)

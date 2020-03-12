# -*- coding: utf-8 -*-

import pygame
import random

clock = pygame.time.Clock()
time_passed = clock.tick()
time_passed = clock.tick(30)

win_w, win_h = 600, 500
ball_r = 30


def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))


def init_ball():
    return random.randint(ball_r, win_w - ball_r), 0

#1. 游戏启动，和小球下落
#2. 控制挡板
#3. 添加分数
#4. 其它扩展

def playGame(screen, lives, score):
    # ball_x, ball_y = 0, 100
    # 小挡板的坐标和宽高
    rect_x, rect_y, rect_w, rect_h = (win_w - 120) / 2, win_h - 40, 120, 40

    font1 = pygame.font.Font(None, 24)

    # 让小球从一个上面随机的位置出现

    ball_x, ball_y = init_ball()
    vel_y = 4  # 小球的初始下落速度
    # 我们需要一个白色的背景界面
    white = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:  # 监听鼠标动作
                rect_x, _ = event.pos  # 让小挡板始终都和鼠标一起动
                rect_x -= rect_w / 2
                if rect_x < 0:
                    rect_x = 0
                elif rect_x > win_w - rect_w:
                    rect_x = win_w - rect_w

        if rect_y - ball_y < ball_r:
            if rect_x < ball_x < rect_x + rect_w:
                score += 1
            else:
                lives -= 1
                if lives == 0:
                    break
            ball_x, ball_y = init_ball()
        else:
            ball_y += vel_y

        screen.fill(white)
        pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), ball_r, 0)
        pygame.draw.rect(screen, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        print_text(screen, font1, 50, 50, str(lives))
        print_text(screen, font1, 300, 50, str(score))

        pygame.display.update()
        time_passed = clock.tick(30)


def main():
    pygame.init()
    screen = pygame.display.set_mode((win_w, win_h))
    pygame.display.set_caption('BALL')
    lives = 3
    score = 0
    playGame(screen, lives, score)



if __name__ == '__main__':
    main()

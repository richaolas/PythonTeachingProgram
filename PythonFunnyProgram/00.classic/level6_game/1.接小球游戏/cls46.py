'''
启动和结束画面
'''

import random

import pygame

WIDTH = 600
HEIGHT = 500
R = 20
FPS = 30
SPEED = 200

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game variable
life = 3
score = 0
padding = 10
game_over = False

# 初始化引擎
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# if using chinese
# lst = pygame.font.get_fonts()
# font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 25)

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y, color=(255, 255, 255), align=0):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == 0:  # left align
        text_rect.topleft = (x, y)
    elif align == 1:  # right align
        text_rect.topright = (x, y)
    elif align == 2:  # mid align
        text_rect.midtop = (x, y)

    surf.blit(text_surface, text_rect)


# ball = pygame.Surface((2 * R, 2 * R))
# ball.fill(BLACK)
# ball.set_colorkey(BLACK)
# pygame.draw.circle(ball, RED, (R, R), R)
# ball = ball.convert()
# rect = ball.get_rect()
# rect.midtop = (WIDTH / 2, 0)

block_width, block_height = 100, 20
block = pygame.Surface((block_width, block_height))
block.fill((128, 60, 24))
block_rect = block.get_rect()
block_rect.midtop = (WIDTH / 2, HEIGHT - block_height)

balls = []
mouse_x, mouse_y = WIDTH / 2, 0

last_time = pygame.time.get_ticks()


def gen_ball(current_time, rate=1000):
    global last_time
    if current_time > last_time + rate:
        last_time = current_time
        x = random.randint(R, WIDTH - R)
        y = -R
        ball = pygame.Surface((2 * R, 2 * R))
        ball.fill(BLACK)
        ball.set_colorkey(BLACK)
        pygame.draw.circle(ball, RED, (R, R), R)
        ball = ball.convert()
        rect = ball.get_rect()
        rect.center = (x, y)
        balls.append({'ball': ball, 'rect': rect})


def show_go_screen():
    screen.fill((0, 0, 0))
    draw_text(screen, "Catch The Ball!", 64, WIDTH / 2, HEIGHT / 4, (255,255,255), 2)
    draw_text(screen, "Using mouse to control the block", 22, WIDTH / 2, HEIGHT / 2, (255,255,255), 2)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4, (255,255,255), 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
        #screen.fill((0,0,0))
        #draw_text(screen, "Catch The Ball!", 64, WIDTH / 2, HEIGHT / 4)
        #pygame.display.flip()
        #print('#s')

show_go_screen()

while True:

    if game_over:
        show_go_screen()
        life = 3
        score = 0
        game_over = False
        balls = []

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            # return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
    # 填充屏幕背景
    screen.fill((0, 0, 0))

    gen_ball(ticks, 1000)

    block_rect.x = max(0, min(WIDTH - block_width, mouse_x - block_width / 2))

    valid = []
    for kv in balls:
        # kv['rect'].y += 5
        kv['rect'].y += time_passed_seconds * SPEED  # 这种方式，无论是否能达到fps，都能在不同电脑上相似的执行

        if block_rect.colliderect(kv['rect']):
            score += 10
        elif kv['rect'].bottom > HEIGHT:
            life -= 1
            if life == 0:
                game_over = True
        else:
            valid.append(kv)
            screen.blit(kv['ball'], kv['rect'])
    balls = valid

    screen.blit(block, block_rect)

    # 渲染文字
    draw_text(screen, "Life: {0}".format(life), 24, padding, padding, WHITE)
    draw_text(screen, "Score: {0}".format(score), 24, WIDTH - padding, padding, WHITE, 1)

    # 渲染屏幕
    pygame.display.update()

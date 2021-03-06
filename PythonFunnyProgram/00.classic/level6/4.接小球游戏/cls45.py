'''
pygame 接球逻辑
'''
import random
import pygame

pygame.init()
WIDTH = 600
HEIGHT = 500
life = 3
score = 0
padding = 10
lst = pygame.font.get_fonts()
# print lst
print(lst)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 25)

mouse_x = WIDTH / 2
mouse_y = 0

board_width = 100
borad_height = 30
board_x = (WIDTH - board_width) / 2

balls = []
R = 20
SPEED = 200

last_time = pygame.time.get_ticks()


def gen_ball(current_time, rate=60):
    global last_time
    if current_time > last_time + rate:
        last_time = current_time
        x = random.randint(R, WIDTH - R)
        balls.append([x, 0])


def update(time):
    global balls, score, life
    tmp = []
    for pos in balls:
        pos[1] += time * SPEED
        if board_x < pos[0] < board_x + board_width and pos[1] + R >= HEIGHT - borad_height:
            score += 1
        else:
            if pos[1] < HEIGHT + R:
                tmp.append(pos)
            else:
                life -= 1

    balls = tmp


clock = pygame.time.Clock()

while True:
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            # return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]


    gen_ball(ticks, 3000)
    update(time_passed_seconds)

    liftText = font.render("生命: {0}".format(life), True, (100, 200, 0))
    scoreText = font.render("分数: {0}".format(score), True, (100, 200, 0))

    screen.fill((0, 0, 0))
    screen.blit(liftText, (padding, padding))
    screen.blit(scoreText, (WIDTH - padding - scoreText.get_width(), padding))

    for pos in balls:
        pygame.draw.circle(screen, (255, 0, 0), (int(pos[0]), int(pos[1])), R)

    board_x = max(0, min(WIDTH - board_width, mouse_x - board_width / 2))
    pygame.draw.rect(screen, (200, 100, 30),
                     (board_x, HEIGHT - borad_height, board_width, borad_height), 0)

    pygame.display.update()

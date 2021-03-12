'''
pygame 接球逻辑
'''
import random
import pygame

pygame.init()
FPS = 30
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

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():
    screen.fill((0, 0, 0))
    draw_text(screen, "Catch The Ball!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Using mouse to control the block", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

clock = pygame.time.Clock()

while True:

    if life == 0:
        show_go_screen()
        life = 3
        balls = []
        board_x = (WIDTH - board_width) / 2


    time_passed = clock.tick(FPS)
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

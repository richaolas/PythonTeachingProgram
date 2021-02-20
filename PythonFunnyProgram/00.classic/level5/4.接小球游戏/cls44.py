import pygame
import random

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
mouse_x = WIDTH/2
mouse_y = 0

board_width = 100
borad_height = 30

balls = []
R = 20
SPEED = 10

def gen_ball():
    y = 0
    x = random.randint(R, WIDTH-R)
    balls.append([x, y])

def update():
    global balls
    tmp = []
    for pos in balls:
        pos[1] += SPEED
        if pos[1] < HEIGHT + R:
            tmp.append(pos)
    balls = tmp


clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            # return the X and Y position of the mouse cursor
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
    screen.fill((0, 0, 0))

    gen_ball()
    update()

    liftText = font.render("生命: {0}".format(life), True, (100, 200, 0))
    scoreText = font.render("分数: {0}".format(score), True, (100, 200, 0))
    screen.blit(liftText, (padding, padding))
    screen.blit(scoreText, (WIDTH-padding-scoreText.get_width(), padding))
    
    for pos in balls:
        pygame.draw.circle(screen, (255,0,0), pos, R)
        
    pygame.draw.rect(screen, (200, 100, 30), (mouse_x - board_width/2, HEIGHT - borad_height, board_width, borad_height), 0)

    pygame.display.update()


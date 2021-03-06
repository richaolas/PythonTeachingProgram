'''
pygame 时间处理
'''

import random
import pygame

'''
规则1：小球从上方落下，无论接到或没接到都再次让小球从上方落下。
规则2：接到小球得一分，小球下落的速度随分数增加而变快。
规则3：设共三个生命值，没接到小球则失去一个生命值，生命值为0时游戏结束，显示这次最终得分。
'''

'''
Key function:
0. 速度控制，pixel per sec
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0
    
    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds  
1. 每隔一段时间，落下一个小球
2. 隔一段时间，间隔缩短，速度变快

time:
time_passed = clock.tick(30) # 相对时间
ticks = pygame.time.get_ticks() # 绝对时间

'''

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
    global balls
    tmp = []
    for pos in balls:
        pos[1] += time * SPEED
        if pos[1] < HEIGHT + R:
            tmp.append(pos)
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
    board_x = max(0, min(WIDTH-board_width, mouse_x - board_width / 2))
    pygame.draw.rect(screen, (200, 100, 30),
                     (board_x, HEIGHT - borad_height, board_width, borad_height), 0)

    pygame.display.update()

'''
def update(self, current_time, rate=60):
# #         if current_time > self.last_time + rate:
# #             self.frame += 1
# #             if self.frame > self.last_frame:
# #                 self.frame = self.first_frame
# #             self.last_time = current_time
# #
# #         if self.frame != self.old_frame:
# #             frame_x = (self.frame % self.columns) * self.frame_width
# #             frame_y = (self.frame // self.columns) * self.frame_height
# #             rect = (frame_x, frame_y, self.frame_width, self.frame_height)
# #             self.image = self.master_image.subsurface(rect)
# #             self.old_frame = self.frame
# #
# #
# # pygame.init()
# # screen = pygame.display.set_mode((800, 600), 0, 32)
# # pygame.display.set_caption("精灵类测试")
# # font = pygame.font.Font(None, 18)
# # framerate = pygame.time.Clock()
# #
# # cat = MySprite(screen)
# # cat.load("sprite.png", 100, 100, 4)
# # group = pygame.sprite.Group()
# # group.add(cat)
# #
# # while True:
# #     x = framerate.tick(30) # 相对时间
# #     ticks = pygame.time.get_ticks() # 绝对时间

'''

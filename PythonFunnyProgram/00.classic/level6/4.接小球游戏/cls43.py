'''
pygame 显示文字
'''

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
#default_font = pygame.font.get_default_font()
#font = pygame.font.SysFont(default_font, 24)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0, 0, 0))
    liftText = font.render("生命: {0}".format(life), True, (100, 200, 0))
    scoreText = font.render("分数: {0}".format(score), True, (100, 200, 0))
    screen.blit(liftText, (padding, padding))
    screen.blit(scoreText, (WIDTH-padding-scoreText.get_width(), padding))
    pygame.display.update()

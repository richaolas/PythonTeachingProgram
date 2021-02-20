import pygame
pygame.init()

screen = pygame.display.set_mode((600, 500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (100, 100, 30), (100, 100), 30, 0)
    pygame.display.update()

'''
Objects
'''

# put Python classes and functions here

'''
Setup
'''

# put run-once code here

'''
Main Loop
'''

# put game loop here

# the pygame template

# Pygame template - skeleton for a new pygame project
import pygame
import random

class DummySprite(pygame.sprite.Sprite):
    def __init__(self, image, location):
        super().__init__()
        self.image = image
        rect = self.image.get_rect()
        rect.x, rect.y = location
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)
        pass





WIDTH = 360
HEIGHT = 480
FPS = 30 # frame per second

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

role = DummySprite(pygame.image.load('role01_min.png'), (0,0))
ball = DummySprite(pygame.image.load('ball_min.png'), (200,0))
# role = pygame.image.load('role01_min.png')
# role_rect = role.get_rect()
#
# ball = pygame.image.load('ball_min.png')
# ball_rect = ball.get_rect()
# X = 200
# ball_rect.x = X
# Game loop
running = True

group = pygame.sprite.Group()
group.add(ball)

while running:
    # keep loop running at the right speed
    clock.tick(FPS) #隐藏fps来说明update原理
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    # X -= 0.5
    #
    # screen.blit(role, (0,0))
    # pygame.draw.rect(screen,(255,0,0), role_rect, 2)
    #
    # ball_rect = ball.get_rect()
    # ball_rect.x = X
    # screen.blit(ball, (X,0))
    # pygame.draw.rect(screen, (255,0,0), ball_rect, 2)
    screen.blit(role.image, role.rect)
    pygame.draw.rect(screen, (255, 0, 0), role.rect, 2)


    screen.blit(ball.image, ball.rect)
    pygame.draw.rect(screen, (255, 0, 0), ball.rect, 2)

    ret = pygame.sprite.collide_rect(role, ball)
    ret2 = pygame.sprite.spritecollide(role, group, False, pygame.sprite.collide_mask)
    print(ret, ret2)
    if ret2:
        print(id(ret2[0]), id(role), id(ball))

    if (not ret) or (not ret2):
        ball.rect.x -= 0.5

    #if (not ret) :
    #    ball.rect.x -= 0.5

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

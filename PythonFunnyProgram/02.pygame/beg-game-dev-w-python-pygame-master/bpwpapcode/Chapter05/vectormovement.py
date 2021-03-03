background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

from sys import exit

import pygame
from pygame.locals import *
# from gameobjects.vector2 import Vector2
from pygame.math import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.fill((255,255,255))

    if position.x < 639 and position.y < 479:
        screen.blit(sprite, ((int)(position.x), (int)(position.y)))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    #destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2
    destination = Vector2(639, 479) - Vector2(*sprite.get_size()) / 2

    vector_to_mouse = Vector2(position, destination)
    vector_to_mouse.normalize()

    # speed is quicker
    heading = heading + (vector_to_mouse * .6)

    position += heading * time_passed_seconds
    pygame.display.update()

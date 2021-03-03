#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)


while True:
        
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    '''
    Not all surfaces need to be locked. Hardware surfaces do (the screen is usually a hardware
    surface), but plain software surfaces do not. Pygame provides a mustlock method in surface
    objects that returns True if a surface requires locking. You could check the return value of
    mustlock before you do any locking or unlocking, but there is no problem in locking a surface that
    doesn’t need it, so you may as well lock any surface that you plan on doing a lot of drawing to.
    '''
    screen.lock()
    for count in range(10):
        random_color = (randint(0,255), randint(0,255), randint(0,255))        
        random_pos = (randint(0,639), randint(0,479))
        random_size = (639-randint(random_pos[0],639), 479-randint(random_pos[1],479))    
        pygame.draw.rect(screen, random_color, (random_pos, random_size))
    screen.unlock()
        
    pygame.display.update()
    
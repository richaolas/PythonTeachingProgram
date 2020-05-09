import turtle

w = turtle.window_width()
h = turtle.window_height()

turtle.forward(100)
turtle.circle(50, 100)

turtle.done()

import time
import turtle
#from playsound import playsound
import pygame

turtle.speed(0)

turtle.setup(800, 600, 100, 100)
turtle.write('10:00'*10, font=('Arial',30,'normal'))

turtle.color('black')
#turtle.fillcolor('')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.setheading(90)
turtle.pensize(10)
turtle.circle(-200, 90)

time.sleep(3)
turtle.clear()
#turtle.speed(1)
turtle.color('red')
a = 30
turtle.begin_fill()
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(100,0)
turtle.goto(a,-a)
turtle.goto(0, -100)
turtle.goto(-a,-a)
turtle.goto(-100,0)
turtle.goto(-a,a)
turtle.goto(0,100)
turtle.goto(a,a)
turtle.goto(100,0)
turtle.end_fill()

# turtle.circle(200)

turtle.done()


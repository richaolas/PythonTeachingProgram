import turtle
import time

turtle.speed(0)

r = 50
for i in range(3):
    turtle.circle(r, 360)
    turtle.right(90)
    if i != 2:
        turtle.circle(r, 360)
        turtle.left(90)
        turtle.penup()
        turtle.forward(2*r)
        turtle.pendown()
turtle.done()
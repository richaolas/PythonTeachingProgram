import turtle
import random

span = 20
max_radius = 150
turtle.colormode(255)
turtle.speed(0)

a = 0
while a < 5:
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    # turtle.fillcolor(r, g, b)
    # turtle.pencolor(r, g, b)
    turtle.color((0, 0, 0), (r, g, b))
    turtle.begin_fill()
    turtle.circle(max_radius - span * a)
    turtle.end_fill()
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(span)
    turtle.pendown()
    turtle.setheading(0)
    a = a + 1

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.setheading(270)
turtle.pensize(20)
turtle.forward(180)

turtle.done()

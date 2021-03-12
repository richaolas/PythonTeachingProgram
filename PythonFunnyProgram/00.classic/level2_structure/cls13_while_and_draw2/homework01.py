import turtle
import random

turtle.colormode(255)

count = 0
a = 300
N = 10

while count < N:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.fillcolor(r, g, b)
    turtle.begin_fill()
    turtle.goto(a, 0)
    turtle.goto(0, a)
    turtle.goto(0, 0)
    turtle.end_fill()
    a -= 30
    count = count + 1

turtle.done()

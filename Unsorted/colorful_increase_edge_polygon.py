import turtle
import random

for i in range(3, 21):
    turtle.fillcolor(random.random(), random.random(), random.random())
    turtle.begin_fill()
    for n in range(i):
        turtle.forward(20)
        turtle.left(360 / i)
    turtle.end_fill()
turtle.done()

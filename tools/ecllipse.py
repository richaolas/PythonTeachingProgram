import turtle
import math

s = turtle.speed()
turtle.speed(0)
print(s)
def ellipse(a, b, angle=50, steps=1):
    minAngle = (2 * math.pi / 360) * angle / steps
    turtle.penup()
    turtle.setpos(0, -b)
    turtle.pendown()
    for i in range(steps):
        nextPoint = [a * math.sin((i + 1) * minAngle), -b * math.cos((i + 1) * minAngle)]
        turtle.setpos(nextPoint)
turtle.speed(s)

ellipse(100,50,360,360)

turtle.done()
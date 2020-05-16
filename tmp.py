<<<<<<< HEAD
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
=======


import turtle
import random
w=turtle.window_width()
h=turtle.window_height()
a = 1
turtle.speed(0)
turtle.colormode(255)
sum=0
counter=0
while a<=50:

    x=random.randint(-1/2*w,w/2)
    y=random.randint(-h/2,h/2)
    r=random.randint(30,80)
    if r <40:
        sum=3.14*r*r+sum
        counter=counter+1

    turtle.penup()
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)
    a = a + 1
print(counter,sum/counter)


turtle.done()
>>>>>>> 14829a43750c03c6bb433ee59c75c359a437c774

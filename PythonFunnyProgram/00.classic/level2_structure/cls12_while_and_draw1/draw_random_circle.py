
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
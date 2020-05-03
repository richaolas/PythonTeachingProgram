import turtle
import random
a=1
r=20
turtle.colormode(255)
while a<6:
    r1 = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    turtle.fillcolor(r1, g, b)
    turtle.pencolor(r1, g, b)
    turtle.begin_fill()
    turtle.circle(150-r*a)
    turtle.end_fill()
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.setheading(0)




    a=a+1
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.setheading(270)
turtle.pensize(20)
turtle.forward(180)

turtle.done()

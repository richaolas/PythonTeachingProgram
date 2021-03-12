import turtle

n = 0
a = 20
N = 20

turtle.speed(0)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.left(90)
turtle.pensize(3)
turtle.forward(a*4)

turtle.color('red')

while n < N:
    turtle.dot(a)
    n = n + 1
    if n < N:
        turtle.forward(a)

turtle.done()

import turtle

n = 0
a = 40

turtle.speed(0)

turtle.color('black', 'red')
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

while n < 4:
    turtle.begin_fill()
    turtle.circle(a)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.forward(a * 2)
    turtle.left(90)
    turtle.pendown()
    n = n + 1
    
turtle.pensize(10)
turtle.penup()
turtle.left(90)
turtle.forward(a * 2)
turtle.right(180)
turtle.pendown()
turtle.forward(a * 4)

turtle.done()

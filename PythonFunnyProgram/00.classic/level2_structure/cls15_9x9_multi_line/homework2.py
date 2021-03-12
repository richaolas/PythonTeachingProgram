import turtle

a = 10
d = 5
turtle.pencolor('red')
for i in range(32):
    turtle.penup()
    turtle.forward(a)
    turtle.pendown()
    turtle.dot(d)
    if i % 4 == 0:
        d += 4
    a += 12
    turtle.left(93)

turtle.done()
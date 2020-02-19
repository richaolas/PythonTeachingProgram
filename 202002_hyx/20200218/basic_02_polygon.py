import turtle

n = 8

for i in range(n):
    turtle.forward(100)
    turtle.left(360 / n)

turtle.done()
import turtle

n = 0
turtle.speed(0)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.begin_fill()
while n < 25:
    turtle.circle(30)
    turtle.right(20)
    n = n+1

turtle.end_fill()
turtle.setheading(270)
turtle.forward(200)

turtle.done()
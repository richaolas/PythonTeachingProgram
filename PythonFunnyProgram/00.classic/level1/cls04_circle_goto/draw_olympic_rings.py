import turtle

turtle.speed(0)

# blue, yellow, black, green, red

turtle.pensize(10)
turtle.left(90)

turtle.pencolor('blue')
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.circle(-50)

turtle.pencolor('yellow')
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(-50)

turtle.pencolor('black')
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.circle(-50)

turtle.pencolor('green')
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(-50)

turtle.pencolor('red')
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.circle(-50)

turtle.done()

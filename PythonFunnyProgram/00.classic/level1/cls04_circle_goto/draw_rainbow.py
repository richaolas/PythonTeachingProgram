import turtle

turtle.pensize(20)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.pencolor('red')
turtle.setheading(90)
turtle.circle(-100, 180)

turtle.penup()
turtle.goto(-100+20 -5, 0)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor('yellow')
turtle.circle(-100+20 - 5, 180)

turtle.penup()
turtle.goto(-100+20*2 - 5*2, 0)
turtle.setheading(90)
turtle.pendown()
turtle.pencolor('green')
turtle.circle(-100+20*2 - 5*2, 180)

turtle.done()
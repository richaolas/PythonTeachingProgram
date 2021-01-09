import turtle
import time
turtle.pensize(5)

turtle.forward(90)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(200)

turtle.penup()
turtle.goto(45,160)
turtle.pencolor("red")
turtle.pendown()
turtle.dot(40)

time.sleep(3)
turtle.penup()
turtle.goto(45,110)
turtle.pencolor("yellow")
turtle.pendown()
turtle.dot(40)
time.sleep(3)

turtle.penup()
turtle.goto(45,60)
turtle.pencolor("green")
turtle.pendown()
turtle.dot(40)

turtle.done()
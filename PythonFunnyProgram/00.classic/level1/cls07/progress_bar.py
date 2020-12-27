import turtle
import time

turtle.bgcolor("black")
turtle.pensize(5)
turtle.pencolor("white")
turtle.forward(200)
turtle.circle(10,180)
turtle.forward(200)
turtle.circle(10,180)
turtle.penup()
turtle.goto(0,10)
for i in range(11):
    turtle.dot(26)
    turtle.forward(20)
    time.sleep(1)
turtle.done()
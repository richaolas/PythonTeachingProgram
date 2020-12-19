
import turtle

turtle.speed(0)
turtle.bgcolor('skyblue')
w = turtle.window_width()
h = turtle.window_height()

turtle.fillcolor('blue')
turtle.pencolor('blue')
turtle.begin_fill()

turtle.goto(-w/2, 0)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)

turtle.end_fill()

turtle.begin_fill()
turtle.goto(-200, -10)
turtle.goto(0, 100)
turtle.setheading(180+20)
turtle.circle(100, 180)
turtle.goto(-200, -10)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(200, -10)
turtle.goto(300, 50)
turtle.setheading(180+30)
turtle.circle(100, 180)
turtle.goto(200, -10)
turtle.end_fill()

# turtle.begin_fill()
# turtle.goto(-200, -250)
# turtle.circle(400)
# turtle.end_fill()
# turtle.begin_fill()
# turtle.goto(300, -350)
# turtle.circle(400)
# turtle.end_fill()

turtle.done()

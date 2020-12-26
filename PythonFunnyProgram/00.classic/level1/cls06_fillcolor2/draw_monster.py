import turtle

w = turtle.window_width()
h = turtle.window_height()

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('skyblue')
star_size = 20

# draw star
turtle.penup()
turtle.goto(200, 280)
turtle.pendown()
turtle.pencolor('yellow')
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(star_size)
    turtle.right(144)
    turtle.forward(star_size)
    turtle.left(72)
turtle.end_fill()

# draw sea
turtle.penup()
turtle.goto(-w/2, 0)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)
turtle.right(90)
turtle.end_fill()

# draw monster

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()


turtle.forward(10)
turtle.right(25)
turtle.forward(220)
turtle.left(90)
turtle.forward(130)
turtle.circle(-10, 160)
turtle.circle(-800, 18)
turtle.goto(90, -h/2)
turtle.setheading(180)
turtle.forward(150)
turtle.setheading(110)
turtle.circle(-800, 16.45)
turtle.goto(-100,-100)
# turtle.circle(800,100)
turtle.end_fill()

turtle.penup()
turtle.goto(-70,-160)
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(20, 360)
turtle.end_fill()

turtle.penup()
turtle.goto(-70,-140)
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(10, 360)
turtle.end_fill()

turtle.done()
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.color('#DCDCDC')
turtle.penup()
turtle.goto(-150, 200)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-150, -150)
turtle.goto(0, -300)
turtle.goto(150, -150)
turtle.goto(150, 200)
turtle.goto(-150, 200)
turtle.end_fill()

a = 30
turtle.color('#CDAD00')
turtle.penup()
turtle.goto(-150 + a, 200 - a)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-150 + a, -150)
turtle.goto(0, -300 + a)
turtle.goto(150 - a, -150)
turtle.goto(150 - a, 200 - a)
turtle.goto(-150 + a, 200 - a)
turtle.end_fill()

turtle.pencolor('#000000')
turtle.pensize(5)

b = 20
turtle.penup()
turtle.goto(-150 + a + b, 200 - a)
turtle.pendown()
turtle.goto(-150 + a + b, -150 - b)
b = 40
turtle.penup()
turtle.goto(-150 + a + b, 200 - a)
turtle.pendown()
turtle.goto(-150 + a + b, -150 - b)
b = 150 - a
turtle.penup()
turtle.goto(-150 + a + b, 200 - a)
turtle.pendown()
turtle.goto(-150 + a + b, -150 - b)

turtle.done()

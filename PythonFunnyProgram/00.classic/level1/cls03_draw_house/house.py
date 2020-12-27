import turtle

turtle.hideturtle()

turtle.color('white','white')
turtle.forward(100)

turtle.color('black','red')
turtle.pensize(10)
turtle.begin_fill()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

turtle.color('black','green')
turtle.pensize(30)
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(-100,0)
turtle.end_fill()

turtle.pensize(10)
turtle.goto(-100,-200)
turtle.forward(50)

turtle.color('black','brown')
turtle.begin_fill()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

turtle.left(180)
turtle.forward(75)
turtle.left(90)
turtle.forward(10)
turtle.dot(20)

turtle.color('black','black')
turtle.left(180)
turtle.forward(10)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)

turtle.pu()
turtle.goto(50,-50)
turtle.pd()

turtle.pensize(5)
turtle.color('black','blue')
turtle.begin_fill()
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()

turtle.pu()
turtle.goto(-50,50)
turtle.pd()

turtle.pensize(30)
turtle.goto(-50,150)

turtle.pu()
turtle.goto(-25,175)
turtle.pd()

turtle.color('grey')
turtle.dot(25)

turtle.pu()
turtle.goto(25,225)
turtle.pd()

turtle.dot(50)

turtle.pu()
turtle.goto(75,275)
turtle.pd()

turtle.dot(75)

turtle.done()
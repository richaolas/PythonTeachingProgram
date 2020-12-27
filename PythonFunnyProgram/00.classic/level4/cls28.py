import turtle

def face():
    turtle.color('black', 'blue')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.color('black', 'white')

    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()

#眼珠
def eye():
    turtle.penup()
    turtle.fillcolor('white')
    for i in [-1, 1]:
        turtle.goto(20 * i, 140)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(10 * i, 160)
        turtle.pendown()
        turtle.dot(10)
        turtle.penup()

#鼻子
def nose():
    turtle.penup()
    turtle.goto(0, 120)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(12, 360, 30)
    turtle.end_fill()
    turtle.penup()

#嘴巴
def mouth():
    turtle.pendown()
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.circle(110, -40)
    turtle.circle(110, 80)
    turtle.right(40)

#胡须
def beard():
    turtle.left(40)
    for i in [1,-1]:
        for r in range(3):
            turtle.penup()
            turtle.goto(15 * i, 110 - r * 10)
            if not (i == -1 and r == 0):
                turtle.right(20 * i)
            turtle.pendown()
            turtle.forward(50 * i)


turtle.hideturtle()

face()
eye()
nose()
mouth()
beard()

turtle.done()

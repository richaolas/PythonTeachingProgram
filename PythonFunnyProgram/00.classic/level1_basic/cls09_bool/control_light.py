# 密码是123456,左control开，右control关

import turtle

turtle.speed(0)

turtle.hideturtle()
turtle.pu()
turtle.goto(0, -100)
turtle.pd()
turtle.goto(150, -100)
turtle.goto(150, 100)
turtle.goto(-150, 100)
turtle.goto(-150, -100)
turtle.goto(50, -100)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.goto(50, -75)
turtle.goto(-50, -75)
turtle.goto(-50, -125)
turtle.goto(50, -125)
turtle.goto(50, -100)
turtle.end_fill()
turtle.pu()
turtle.goto(0, -112.5)
turtle.pd()
turtle.pu()
turtle.goto(0, 100)
turtle.pd()
turtle.pencolor('grey')
turtle.dot(50)
turtle.pu()
turtle.goto(100, -100)
turtle.pd()
turtle.pencolor('white')
turtle.forward(25)
turtle.backward(25)
turtle.left(45)
turtle.pensize(10)
turtle.pencolor('blue')
turtle.forward(25)
pass_ward = '123456'  # input('请输入密码：')


def turn_on():
    if pass_ward == '123456':
        turtle.pu()
        turtle.goto(125, -75)
        turtle.pd()
        turtle.pencolor('white')
        turtle.goto(100, -100)
        turtle.pencolor('blue')
        turtle.goto(125, -100)
        turtle.pu()
        turtle.goto(0, 100)
        turtle.pd()
        turtle.pencolor('yellow')
        turtle.dot(50)
    else:
        print('密码错误')


def turn_off():
    if pass_ward == '123456':
        turtle.pu()
        turtle.goto(125, -100)
        turtle.pd()
        turtle.pencolor('white')
        turtle.goto(100, -100)
        turtle.pencolor('blue')
        turtle.goto(125, -75)
        turtle.pu()
        turtle.goto(0, 100)
        turtle.pd()
        turtle.pencolor('grey')
        turtle.dot(50)
    else:
        print('密码错误')


turtle.onkey(turn_on, 'Control_L')
turtle.onkey(turn_off, 'Control_R')

turtle.listen()
turtle.done()

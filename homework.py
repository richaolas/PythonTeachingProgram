s = '123'
s[0] = '0'

#
# #上下左右，左开上，右开下，上关上，下关下
#
# import turtle
#
# turtle.speed(0)
#
# turtle.pu()
# turtle.goto(25,125)
# turtle.pd()
# turtle.forward(25)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(25)
# turtle.backward(25)
# turtle.right(90)
# turtle.forward(25)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(300)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(25)
# turtle.left(90)
# turtle.forward(25)
# turtle.pensize(10)
# turtle.pencolor('blue')
# turtle.goto(25,100)
# turtle.goto(-25,75)
# turtle.pensize(1)
# turtle.pencolor('black')
# turtle.backward(25)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(25)
# turtle.pensize(10)
# turtle.pencolor('blue')
# turtle.goto(25,150)
# turtle.pu()
# turtle.goto(0,-100)
# turtle.pd()
# turtle.pencolor('red')
# turtle.dot(50)
# turtle.pencolor('black')
# turtle.write('battery',align='center')
# turtle.pu()
# turtle.goto(150,0)
# turtle.pd()
# turtle.pencolor('grey')
# turtle.dot(75)
#
# dot_color = 'grey'
#
# def a():
#     global dot_color
#     turtle.pu()
#     turtle.goto(25,100)
#     turtle.pd()
#     turtle.pencolor('white')
#     turtle.goto(-25,75)
#     turtle.pensize(10)
#     turtle.pencolor('blue')
#     turtle.goto(25,75)
#     turtle.pu()
#     turtle.goto(150,0)
#     turtle.pd()
#     if dot_color == 'grey':
#         turtle.pencolor('yellow')
#         turtle.dot(75)
#         dot_color = 'yellow'
#     elif dot_color == 'yellow':
#         turtle.pencolor('orange')
#         turtle.dot(75)
#         dot_color = 'orange'
# def b():
#     global dot_color
#     turtle.pu()
#     turtle.goto(25,150)
#     turtle.pd()
#     turtle.pencolor('white')
#     turtle.goto(-25,125)
#     turtle.pensize(10)
#     turtle.pencolor('blue')
#     turtle.goto(25,125)
#     turtle.pu()
#     turtle.goto(150,0)
#     turtle.pd()
#     if dot_color == 'grey':
#         turtle.pencolor('yellow')
#         turtle.dot(75)
#         dot_color = 'yellow'
#     elif dot_color == 'yellow':
#         turtle.pencolor('orange')
#         turtle.dot(75)
#         dot_color = 'orange'
# def c():
#     global dot_color
#     turtle.pu()
#     turtle.goto(25,75)
#     turtle.pd()
#     turtle.pencolor('white')
#     turtle.goto(-25,75)
#     turtle.pensize(10)
#     turtle.pencolor('blue')
#     turtle.goto(25,100)
#     turtle.pu()
#     turtle.goto(150,0)
#     turtle.pd()
#     if dot_color == 'yellow':
#         turtle.pencolor('grey')
#         turtle.dot(75)
#         dot_color = 'grey'
#     elif dot_color == 'orange':
#         turtle.pencolor('yellow')
#         turtle.dot(75)
#         dot_color = 'yellow'
# def d():
#     global dot_color
#     turtle.pu()
#     turtle.goto(25,125)
#     turtle.pd()
#     turtle.pencolor('white')
#     turtle.goto(-25,125)
#     turtle.pensize(10)
#     turtle.pencolor('blue')
#     turtle.goto(25,150)
#     turtle.pu()
#     turtle.goto(150,0)
#     turtle.pd()
#     if dot_color == 'yellow':
#         turtle.pencolor('grey')
#         turtle.dot(75)
#         dot_color = 'grey'
#     elif dot_color == 'orange':
#         turtle.pencolor('yellow')
#         turtle.dot(75)
#         dot_color = 'yellow'
#
#
# turtle.onkey(a,'Right')
# turtle.onkey(b,'Left')
# turtle.onkey(c,'Down')
# turtle.onkey(d,'Up')
#
# turtle.listen()
#
# turtle.done()

import turtle
turtle.speed(0)

for j in range(100):
    for i in range(4):
        if i == 1 and j % 20 == 0: # j in [0,20,40,60,80,100]
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(j)
        turtle.left(90)

turtle.done()
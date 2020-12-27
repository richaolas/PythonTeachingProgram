import turtle
turtle.speed(0)
turtle.hideturtle()
for i in range(4):
    if i % 2 == 0:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.forward(100)
    turtle.left(90)
turtle.mainloop()

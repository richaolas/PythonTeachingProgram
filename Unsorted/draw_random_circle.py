import turtle
import random

# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")

#1 random.random() [0,1]
#2 random.randomint(min,max)  [min, max]

turtle.speed(0)
turtle.hideturtle()
for c in range(30):
    turtle.color()
    r,g,b = random.random(), random.random(), random.random()
    turtle.color((r,g,b)) # turtle.color((r,g,b), (r,g,b))
    #turtle.pencolor(r,g,b)
    #turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    # for i in range(c):
    #     #     turtle.forward(c)
    #     #     turtle.left(360/c)
    turtle.circle(random.randint(10, 40), 360)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(random.randint(-300, 300), random.randint(-300, 300))
    turtle.pendown()

turtle.mainloop()

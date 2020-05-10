import  turtle
import time
turtle.speed(0)
turtle.hideturtle()
a=0
onoff=True
while a<100:
    if a%2==0:
        onoff=True
    else:
        onoff=False
    if onoff:
        #turtle.fillcolor('yellow')
        turtle.color('yellow')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
    else:
        #turtle.fillcolor('blue')
        turtle.color('blue')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

    a=a+1
    time.sleep(0.05)

turtle.done()

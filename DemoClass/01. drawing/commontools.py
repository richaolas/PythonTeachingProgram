import turtle
import math

def ellipse2(x, y, a, b, lean = 0, angle=360, steps=360):
    minAngle = (2 * math.pi / 360) * angle / steps
    cos_lean = math.cos(math.pi / 180 * lean)
    sin_lean = math.sin(math.pi / 180 * lean)

    heading = turtle.heading()
    turtle.penup()
    xx, yy = a * math.cos(0), b * math.sin(0)
    nextPoint = [cos_lean * xx + -sin_lean * yy + x, sin_lean * xx + cos_lean * yy + y]
    turtle.goto(nextPoint)
    #turtle.setheading(0)
    turtle.pendown()

    for i in range(steps):
        xx, yy = a * math.cos((i + 1) * minAngle), b * math.sin((i + 1) * minAngle)
        nextPoint = [cos_lean * xx + -sin_lean * yy + x, sin_lean * xx + cos_lean * yy + y]
        turtle.setpos(nextPoint)

    turtle.penup()
    turtle.goto(x, y)
    # turtle.setheading(0)
    turtle.pendown()
    #turtle.setheading(heading)

def ellipse(a, b, angle=360, steps=360):
    # get
    minAngle = (2 * math.pi / 360) * angle / steps

    heading = turtle.heading()

    lean = heading + 90
    cos_lean = math.cos(math.pi / 180 * lean)
    sin_lean = math.sin(math.pi / 180 * lean)

    a1, b1 = math.cos(math.pi / 180 * heading), math.sin(math.pi / 180 * heading)
    c = [math.cos(math.pi/2) * a1 + -math.sin(math.pi/2) * b1, math.sin(math.pi/2) * a1 + math.cos(math.pi/2) * b1]
    x, y = turtle.xcor() + c[0] * a, turtle.ycor() + c[1] * a

    # turtle.penup()
    # xx, yy = a * math.cos(0+math.pi ), b * math.sin(0+math.pi )
    # nextPoint = [cos_lean * xx + -sin_lean * yy + x, sin_lean * xx + cos_lean * yy + y]
    # turtle.goto(nextPoint)
    # #turtle.setheading(0)
    # turtle.pendown()

    for i in range(steps):
        xx, yy = a * math.cos((i + 1) * minAngle + math.pi), b * math.sin((i + 1) * minAngle + math.pi)
        nextPoint = [cos_lean * xx + -sin_lean * yy + x, sin_lean * xx + cos_lean * yy + y]
        turtle.setpos(nextPoint)
        # turtle.setheading

    # turtle.penup()
    # turtle.goto(x, y)
    # # turtle.setheading(0)
    # turtle.pendown()

if __name__ == '__main__':
    turtle.setheading(90)
    ellipse2(100, 50)
    turtle.done()

#a=0.4
# deta = 0.08
# for i in range(120):
#    if 0<=i<30 or 60<=i<90:
#        a=a+deta
#        t.lt(3) #向左转3度
#        t.fd(a) #向前走a的步长
#    else:
#        a=a-deta
#        t.lt(3)
#        t.fd(a)
# t.end_fill() # 依据轮廓填充
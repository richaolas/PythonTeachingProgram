#import turtle as t

import turtle
import math

s = turtle.speed()
turtle.speed(0)
print(s)

#turtle.shapetransform(1,1,0,0.1)

def ellipse(x, y, a, b, lean = 0, angle=360, steps=360):
    minAngle = (2 * math.pi / 360) * angle / steps
    turtle.penup()
    turtle.left(lean)
    turtle.forward(a)
    turtle.pendown()
    cos_lean = math.cos(math.pi / 180 * lean)
    sin_lean = math.sin(math.pi / 180 * lean)
    for i in range(steps):
        x, y = a * math.cos((i + 1) * minAngle), b * math.sin((i + 1) * minAngle)
        nextPoint = [cos_lean * x + -sin_lean * y, sin_lean * x + cos_lean * y]
        turtle.setpos(nextPoint)

turtle.speed(s)

ellipse(0,0,100,50,45, 180)

turtle.done()

# class T:
#     def f(self, a, b, c, **kwargs):
#         pass
#
# print(t.getmethparlist(getattr(T, 'f')))

#t.done()

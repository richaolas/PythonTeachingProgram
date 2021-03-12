import  turtle
turtle.speed(7)
a=0
onoff=True
while a<100:
    if a%2==0:
        onoff=True
    else:
        onoff=False
    if onoff:
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
    else:
        turtle.fillcolor('blue')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

    a=a+1










#
# onoff = input('input light state: ')
#
# if onoff == 'on':
#     onoff = True
# else:
#     onoff = False
#
# if onoff:
#     turtle.fillcolor('yellow')
#     turtle.begin_fill()
#     turtle.circle(50)
#     turtle.end_fill()
# else:
#     turtle.circle(50)
#

turtle.done()

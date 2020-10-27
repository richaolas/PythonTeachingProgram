import turtle

# set attribute
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)

R = 200
r = 100

# get key point
turtle.penup()
turtle.home()
turtle.setheading(270)
turtle.forward(R)
turtle.setheading(0)
RA = turtle.position()
turtle.circle(R, 360/3)
RB = turtle.position()
turtle.circle(R, 360/3)
RC = turtle.position()

turtle.home()
turtle.setheading(90)
turtle.forward(r)
turtle.setheading(0)
rB = turtle.position()
turtle.circle(-r, 360/3)
rA = turtle.position()
turtle.circle(-r, 360/3)
rC = turtle.position()

turtle.pendown()

#########################
turtle.penup()
turtle.goto(RA)
turtle.pendown()

turtle.color(249, 219, 69)
turtle.begin_fill()
turtle.setheading(0)
turtle.circle(R, 360/3)
turtle.goto(rB)
turtle.setheading(0)
turtle.circle(-r, 360/3)
turtle.goto(RA)
turtle.end_fill()

###################################
turtle.penup()
turtle.goto(RB)
turtle.pendown()

turtle.color(224, 77, 43)
turtle.begin_fill()
turtle.setheading(120)
turtle.circle(R, 360/3)
turtle.goto(rC)
turtle.setheading(-360/3*2)
turtle.circle(-r, 360/3)
turtle.goto(RB)
turtle.end_fill()

########################################
turtle.penup()
turtle.goto(RC)
turtle.pendown()

turtle.color(114, 211, 118)
turtle.begin_fill()
turtle.setheading(360/3*2)
turtle.circle(R, 360/3)
turtle.goto(rA)
turtle.setheading(-360/3)
turtle.circle(-r, 360/3)
turtle.goto(RC)
turtle.end_fill()

# draw inner blue circle
turtle.penup()
turtle.home()
turtle.pendown()
turtle.setheading(270)
turtle.forward(r-15)
turtle.setheading(0)
turtle.color(36, 171, 218)
turtle.begin_fill()
turtle.circle(r-15)
turtle.end_fill()

####################

turtle.done()
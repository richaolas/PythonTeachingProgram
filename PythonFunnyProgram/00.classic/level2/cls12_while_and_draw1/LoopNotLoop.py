import turtle as t

count = 0

t.shape("turtle")
t.pencolor("green")
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)
t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()
while count < 4:
    t.circle(100)
    t.left(90)
    count = count + 1
t.done()

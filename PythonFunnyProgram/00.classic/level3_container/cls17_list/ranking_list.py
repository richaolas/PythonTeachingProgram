import turtle

scores = [930, 630, 370, 770, 1034, 490, 90, 210]

#select sort
for i in range(len(scores) - 1):  # range(len(scores) - 1)
    for j in range(i+1, len(scores)):
        if scores[i] < scores[j]:
            scores[i], scores[j] = scores[j], scores[i]

print(scores)

maxLen = 400
height = 30

x = -maxLen/2
y = 200

turtle.hideturtle()
turtle.pensize(height)

for s in scores:
    turtle.color('blue')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(maxLen / scores[0] * s)
    turtle.penup()
    turtle.forward(height)
    turtle.pendown()
    turtle.color('red')
    turtle.write(s,font=('arial',20,'normal'))
    y = y - height * 2

turtle.done()

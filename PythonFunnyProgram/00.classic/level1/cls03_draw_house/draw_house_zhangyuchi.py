import turtle

#hello 张予篪，如果看到这个那就没错是你的代码了，
#我们可以在发挥你的想象力，再填充一些丰富的图案，我会把你的漂亮的小房子保留到git当中的 :)

turtle.color('white','white')
turtle.forward(100)

turtle.color('black','blue')
turtle.pensize(10)
turtle.begin_fill()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

turtle.color('black','green')
turtle.pensize(30)
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(-100,0)
turtle.end_fill()

turtle.pensize(10)
turtle.goto(-100,-200)
turtle.forward(50)

turtle.color('black','brown')
turtle.begin_fill()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

turtle.right(180)
turtle.forward(75)
turtle.left(90)
turtle.forward(10)
turtle.dot(20)

turtle.done()

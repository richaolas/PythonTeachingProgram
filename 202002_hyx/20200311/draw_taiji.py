import turtle

turtle.speed(6)

def draw(radius, color1, color2):
    turtle.width(3)
    turtle.color("black", color1)
    turtle.begin_fill()
    turtle.circle(radius/2, 180)
    turtle.circle(radius, 180)
    turtle.left(180)
    turtle.circle(-radius/2, 180)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(radius * 0.5 * 0.75)
    turtle.right(90)
    turtle.pendown()
    turtle.color(color1, color2)
    turtle.begin_fill()
    turtle.circle(radius * 0.5 * 0.25)
    turtle.end_fill()
    turtle.right(90)
    turtle.penup()
    turtle.forward(radius * 0.5 * 0.75)
    turtle.pendown()
    turtle.right(90)

draw(200, 'black', 'white')
draw(200, 'white', 'black')

turtle.up()
turtle.forward(210)
turtle.right(50)
turtle.down()

draw(80, 'red', 'green')
draw(80, 'blue', 'yellow')

turtle.done()
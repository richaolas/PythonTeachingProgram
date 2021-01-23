# importing package
import turtle

# use forward by 100 (deault = black)
turtle.pensize(5)
# using RGB color, there are 1 and 255 type model, 1 means 0-1 as value of RGB, 255 means 0-255 as value of RGB
turtle.colormode(255)

turtle.color("red")
turtle.forward(100)

# change the color of turtle
# RGB	247	151	198
turtle.color("#F797C6")

# use forward by 100 in 90 degrees
# right (color = red)
turtle.right(90)
turtle.forward(100)

# change the color of turtle
turtle.color((41, 41, 253))

# use forward by 100 in 90 degrees
# right (color = blue)
turtle.right(90)
turtle.forward(100)

# change the color of turtle
turtle.color(41, 253, 41)

# use forward by 100 in 90 degrees
# right (color = green)
turtle.right(90)
turtle.forward(100)

turtle.done()
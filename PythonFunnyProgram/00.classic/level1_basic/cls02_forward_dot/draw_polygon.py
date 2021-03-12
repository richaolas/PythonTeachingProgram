import turtle

edge_count = 5
turn_angle = 180 - ((edge_count - 2) * 180 / edge_count)

turtle.forward(100)
turtle.left(turn_angle)
turtle.forward(100)
turtle.left(turn_angle)
turtle.forward(100)
turtle.left(turn_angle)
turtle.forward(100)
turtle.left(turn_angle)
turtle.forward(100)
turtle.left(turn_angle)

turtle.done()
import turtle

color_pane = {'lt': None, 'padding': 10, 'color_r': 25, 'width': None, 'height': None}
colors = ('green', 'red', 'blue', 'yellow', 'black', 'pink')

color_centers = {}

width = turtle.window_width()
height = turtle.window_height()

def lt ():
    color_pane['width'] = color_pane['padding'] * 2 + color_pane['color_r'] * 2
    color_pane['height'] = (color_pane['padding'] + 2 *color_pane['color_r']) * len(colors) + color_pane['padding']

    x = width / 2 - color_pane['width'] - color_pane['padding']
    y = color_pane['height'] / 2

    color_pane['lt'] = (x, y)

    turtle.penup()
    turtle.goto(color_pane['lt'])
    turtle.pendown()

    for i in range(2):
        turtle.forward(color_pane['width'])
        turtle.right(90)
        turtle.forward(color_pane['height'])
        turtle.right(90)
    pass

def color_dot():
    turtle.forward(color_pane['width'] / 2)
    turtle.right(90)
    turtle.penup()
    turtle.backward(color_pane['color_r'])
    for i in (colors):
        turtle.forward(color_pane['padding'] + color_pane['color_r'] * 2)
        turtle.pencolor(i)
        turtle.pendown()
        turtle.dot(color_pane['color_r'] * 2)
        turtle.penup()
    pass

lt()
color_dot()
turtle.done()
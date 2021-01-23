import turtle

state = {'turn': 5, 'radius': 100, 'width': 20, 'length': 160, }


def init():
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.width(state['width'])


def update():
    turtle.right(state['turn'])


def draw():
    turtle.clear()
    # draw three dot (diameter)
    for c in ('red', 'blue', 'green'):
        turtle.forward(state['length'])
        turtle.color(c)
        turtle.dot(state['radius'] * 2)
        turtle.color('black')
        turtle.backward(state['length'])
        turtle.left(360 / 3)
    turtle.update()


def flush():
    update()
    draw()
    turtle.ontimer(flush, 100)


init()
flush()

turtle.done()

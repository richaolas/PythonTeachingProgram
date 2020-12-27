import turtle

state = {'turn': 5, 'radius': 100, 'width': 20, 'length': 160, }


def spinner():
    # 清空画布
    turtle.clear()
    turtle.width(state['width'])
    angle = state['turn']
    turtle.right(angle)

    # draw three dot (diameter)
    for c in ('red', 'blue', 'green'):
        turtle.forward(state['length'])
        turtle.color(c)
        turtle.dot(state['radius'] * 2)
        turtle.color('black')
        turtle.backward(state['length'])
        turtle.left(120)

    # draw the 'wind'

    turtle.update()


def animate():
    spinner()
    # 请使用ontimer循环调用animate
    turtle.ontimer(animate, 50)


turtle.hideturtle()
turtle.tracer(False)
animate()

turtle.done()

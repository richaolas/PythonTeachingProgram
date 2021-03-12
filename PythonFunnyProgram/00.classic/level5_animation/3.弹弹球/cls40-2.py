import turtle

state = {1: 0, 2: 0}

L = 100
W = 20
SPEED = 20
WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()

left_pen, right_pen = None, None


def init():
    global left_pen, right_pen
    left_pen = turtle.Pen()
    left_pen.pensize(2)
    left_pen.color('black', 'blue')
    left_pen.hideturtle()

    right_pen = turtle.Pen()
    right_pen.pensize(2)
    right_pen.color('black', 'red')
    right_pen.hideturtle()

    turtle.hideturtle()
    turtle.tracer(False)
    turtle.penup()
    turtle.onkeypress(lambda: move(1, 20), 'w')
    turtle.onkeypress(lambda: move(1, -20), 's')
    turtle.onkeypress(lambda: move(2, 20), 'Up')
    turtle.onkeypress(lambda: move(2, -20), 'Down')
    turtle.listen()


def move(player, change):
    state[player] += change


def draw_board(pen, player):
    pen.clear()
    if player == 1:
        lx = -WIDTH / 2
    elif player == 2:
        lx = WIDTH / 2 - W
    ly = state[player] - L / 2
    pen.penup()
    pen.goto(lx, ly)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(W)
        pen.right(90)
        pen.forward(L)
        pen.right(90)
    pen.end_fill()


def draw():
    # 绘制挡板
    draw_board(left_pen, 1)
    draw_board(right_pen, 2)
    turtle.update()


def flush():
    draw()
    turtle.ontimer(flush, 100)


init()
flush()

turtle.done()

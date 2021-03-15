import turtle

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()

BOARD_LEN = 100
BOARD_WIDTH = 20
BOARD_SPEED = 20

board_loc = [0, 0]  # left_board mid-y coordinate, right_board mid-y coordinate
LEFT_BOARD = 0
RIGHT_BOARD = 1

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
    turtle.onkeypress(lambda :board_move(LEFT_BOARD, BOARD_SPEED), 'w')
    turtle.onkeypress(lambda :board_move(LEFT_BOARD, -BOARD_SPEED), 's')
    turtle.onkeypress(lambda :board_move(RIGHT_BOARD, BOARD_SPEED), 'Up')
    turtle.onkeypress(lambda :board_move(RIGHT_BOARD, -BOARD_SPEED), 'Down')
    turtle.listen()


def board_move(board, dis):
    board_loc[board] += dis


# def left_board_up():
#     board_loc[LEFT_BOARD] += BOARD_SPEED
#
#
# def left_board_down():
#     board_loc[LEFT_BOARD] += -BOARD_SPEED
#
#
# def right_board_up():
#     board_loc[RIGHT_BOARD] += BOARD_SPEED
#
#
# def right_board_down():
#     board_loc[RIGHT_BOARD] += -BOARD_SPEED


def draw_board(pen, player):
    pen.clear()
    if player == LEFT_BOARD:
        lx = -WIDTH / 2
    elif player == RIGHT_BOARD:
        lx = WIDTH / 2 - BOARD_WIDTH
    ly = board_loc[player] + BOARD_LEN / 2
    pen.penup()
    pen.goto(lx, ly)
    pen.pendown()
    pen.begin_fill()
    for i in range(2):
        pen.forward(BOARD_WIDTH)
        pen.right(90)
        pen.forward(BOARD_LEN)
        pen.right(90)
    pen.end_fill()


def update():
    pass


def draw():
    # 绘制挡板
    draw_board(left_pen, LEFT_BOARD)
    draw_board(right_pen, RIGHT_BOARD)
    turtle.update()


def flush():
    update()
    draw()
    turtle.ontimer(flush, 100)


init()
flush()

turtle.done()

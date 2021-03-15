"""
bounce when touch the board

#1. 绘制挡板
#2. 控制挡板
#3. 利用lambda表达式优化程序
#4. 不考虑挡板反弹小球
#5. 考虑左挡板反弹小球
#6. 考虑右挡板反弹小球

"""
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

'''
ball variable
'''
BALL_SPEED = 20
BALL_R = 20
ball_loc = [0, 0]
ball_speed = {'x': BALL_SPEED, 'y': BALL_SPEED}

'''
game status
'''
game_over = False


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
    turtle.onkeypress(lambda: board_move(LEFT_BOARD, BOARD_SPEED), 'w')
    turtle.onkeypress(lambda: board_move(LEFT_BOARD, -BOARD_SPEED), 's')
    turtle.onkeypress(lambda: board_move(RIGHT_BOARD, BOARD_SPEED), 'Up')
    turtle.onkeypress(lambda: board_move(RIGHT_BOARD, -BOARD_SPEED), 'Down')
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


def bounce():
    # if ball_loc[0] <= -WIDTH / 2 + BALL_R:
    #     ball_loc[0] = -WIDTH / 2 + BALL_R
    #     ball_speed['x'] *= -1

    # just handle the left board.
    if ball_loc[0] - BALL_R <= -WIDTH / 2 + BOARD_WIDTH:  # 如果超出挡板控制范围
        if board_loc[LEFT_BOARD] - BOARD_LEN / 2 - BALL_R < ball_loc[1] < \
                board_loc[LEFT_BOARD] + BOARD_LEN / 2 + BALL_R:  # 判断是否在挡板范围内
            ball_loc[0] = -WIDTH / 2 + BOARD_WIDTH + BALL_R  # 设置位置为刚好触碰
            ball_speed['x'] *= -1  # 设置反弹
        else:
            global game_over
            game_over = True

    if ball_loc[0] >= WIDTH / 2 - BALL_R:
        ball_loc[0] = WIDTH / 2 - BALL_R
        ball_speed['x'] *= -1

    if ball_loc[1] <= -HEIGHT / 2 + BALL_R:
        ball_loc[1] = -HEIGHT / 2 + BALL_R
        ball_speed['y'] *= -1

    if ball_loc[1] >= HEIGHT / 2 - BALL_R:
        ball_loc[1] = HEIGHT / 2 - BALL_R
        ball_speed['y'] *= -1


def update():
    ball_loc[0] += ball_speed['x']
    ball_loc[1] += ball_speed['y']
    bounce()


def draw():
    # 绘制挡板
    draw_board(left_pen, LEFT_BOARD)
    draw_board(right_pen, RIGHT_BOARD)
    turtle.clear()
    turtle.goto(ball_loc)
    turtle.dot(2 * BALL_R)
    turtle.update()


def flush():
    update()
    draw()
    if not game_over:
        turtle.ontimer(flush, 50)

    else:
        turtle.home()
        turtle.write('Game Over', align='center', font=('Arial', 40))


init()
flush()

turtle.done()

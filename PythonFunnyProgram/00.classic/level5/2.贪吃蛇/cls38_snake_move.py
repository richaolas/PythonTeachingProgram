import turtle
import random

turtle.hideturtle()
turtle.tracer(False)
turtle.up()
# turtle.colormode(255)

SPEED = 25
SIZE = SPEED
snake = []
direction = {'x': 0, 'y': SPEED}

########################
WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()

bean_pos = [0, 0]
eaten = False
game_over = False


########################

def init():
    for i in range(5):
        snake.append({'x': 0, 'y': -i * SIZE})


def right():
    if direction['x'] == 0:
        direction['x'] = SPEED
        direction['y'] = 0


def left():
    if direction['x'] == 0:
        direction['x'] = -SPEED
        direction['y'] = 0


def up():
    if direction['y'] == 0:
        direction['x'] = 0
        direction['y'] = SPEED


def down():
    if direction['y'] == 0:
        direction['x'] = 0
        direction['y'] = -SPEED


def update():
    global eaten
    global game_over
    # 增加一节
    head = snake[0].copy()
    # print(id(head), id(snake[0]))
    head['x'] += direction['x']
    head['y'] += direction['y']
    snake.insert(0, head)
    del snake[-1]


def draw(color):
    turtle.clear()
    # turtle.pencolor(color)  # 设置画笔颜色
    # for s in snake:
    #    turtle.goto(s['x'], s['y'])  # 移动画笔坐标
    #    turtle.dot(SIZE)  # 绘制一节蛇
    for i, s in enumerate(snake):
        turtle.pencolor(i / len(snake), 0, 0)
        turtle.goto(s['x'], s['y'])  # 移动画笔坐标
        turtle.dot(SIZE)  # 绘制一节蛇


def flush():
    update()
    draw('red')
    if not game_over:
        turtle.ontimer(flush, 100)
    else:
        turtle.home()
        turtle.write('Game Over', align='center', font=('Arial', 40))


init()
flush()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

turtle.done()

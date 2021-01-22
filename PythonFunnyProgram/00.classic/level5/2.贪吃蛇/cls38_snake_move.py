import turtle

turtle.hideturtle()
turtle.tracer(False)
turtle.up()

SPEED = 10
SIZE = SPEED
snake = []
direction = {'x': 0, 'y': SPEED}


def init():
    for i in range(5):
        snake.append({'x': 0, 'y': -i * SIZE})


def right():
    direction['x'] = SPEED
    direction['y'] = 0


def left():
    direction['x'] = -SPEED
    direction['y'] = 0


def up():
    direction['x'] = 0
    direction['y'] = SPEED


def down():
    direction['x'] = 0
    direction['y'] = -SPEED


def draw(color):
    turtle.clear()
    turtle.pencolor(color)  # 设置画笔颜色
    for s in snake:
        turtle.goto(s['x'], s['y'])  # 移动画笔坐标
        turtle.dot(SIZE)  # 绘制一节蛇


def flush():
    # 增加一节
    head = snake[0].copy()
    #print(id(head), id(snake[0]))
    head['x'] += direction['x']
    head['y'] += direction['y']
    snake.insert(0, head)

    # 删除最后一节
    snake.remove(snake[-1])

    draw('red')
    turtle.ontimer(flush, 100)


init()
flush()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

turtle.done()

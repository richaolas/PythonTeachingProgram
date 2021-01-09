import turtle

turtle.hideturtle()
turtle.tracer(False)
turtle.up()

SPEED = 10
SIZE = SPEED
snake = []
direction = {'x': 0, 'y': 10}


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


def move():
    # 改变第一节蛇的坐标
    #for s in snake:
    #    s['x'] += direction['x']
    #    s['y'] += direction['y']
    #tail = snake[-1]
    snake.remove(snake[-1])
    head = snake[0].copy()
    print(id(head), id(snake[0]))
    head['x'] += direction['x']
    head['y'] += direction['y']
    snake.insert(0, head)
    print(snake)

    draw('red')
    turtle.ontimer(move, 50)

init()
move()
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

turtle.done()

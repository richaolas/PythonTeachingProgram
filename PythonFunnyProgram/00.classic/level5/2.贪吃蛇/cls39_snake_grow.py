import random
import turtle

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


def knock(point, points):
    x1, y1 = point['x'], point['y']
    for p in points:
        x2, y2 = p['x'], p['y']
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 < SIZE ** 2:
            return True
    return False


def gen_bean_pos():
    # min_x = min(snake, key=lambda p: p['x'])['x'] - SIZE
    # max_x = max(snake, key=lambda p: p['x'])['x'] + SIZE
    # min_y = min(snake, key=lambda p: p['y'])['y'] - SIZE
    # max_y = max(snake, key=lambda p: p['y'])['y'] + SIZE
    found = False
    W = int(WIDTH / 2 - SIZE / 2)
    H = int(HEIGHT / 2 - SIZE / 2)
    while not found:
        x = random.randint(-W, W)
        y = random.randint(-H, H)
        if not knock({'x': x, 'y': y}, snake):
            bean_pos[0], bean_pos[1] = x, y
            found = True


def can_eat():
    return knock({'x': bean_pos[0], 'y': bean_pos[1]}, snake[0:1])
    # head = snake[0]
    # return (head['x'] - bean_pos[0]) ** 2 + (head['y'] - bean_pos[1]) ** 2 < SIZE ** 2


def knock_wall():
    head = snake[0]
    return (abs(head['x']) > WIDTH / 2 - SIZE / 2) or (abs(head['y']) > HEIGHT / 2 - SIZE / 2)


def knock_self():
    # head = snake[0]
    # for i in range(1, len(snake)):
    #     body = snake[i]
    #     if (head['x'] - body['x']) ** 2 + (head['y'] - body['y']) ** 2 < SIZE ** 2:
    #         return True
    # return False
    return knock(snake[0], snake[1:])


########################

def init():
    for i in range(5):
        snake.append({'x': 0, 'y': -i * SIZE})
    gen_bean_pos()


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

    if eaten:
        gen_bean_pos()
        eaten = False
    else:
        # 删除最后一节
        # 注意python 这个remove，它是按值删除，而不是按索引，这个是经常容易出错的地方
        # snake.remove(snake[-1])
        del snake[-1]

    if can_eat():
        eaten = True

    if knock_wall() or knock_self():
        game_over = True


def draw(color):
    turtle.clear()
    turtle.color('green')
    turtle.goto(bean_pos)
    turtle.dot(SIZE)

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

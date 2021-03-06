import random
import turtle

'''
In the class, we use map present the position 
'''

'''
global variable
'''
WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()

R = 12
SPEED_VALUE = R * 2

snake = []
speed = {'x': 0, 'y': SPEED_VALUE}

'''
new features
'''

bean_pos = {'x': 0, 'y': 0}
eaten = False
game_over = False


def knock(point, points):
    x1, y1 = point['x'], point['y']
    for p in points:
        x2, y2 = p['x'], p['y']
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 < (2 * R) ** 2:
            return True
    return False


def gen_bean_pos():
    found = False
    w = int(WIDTH / 2 - R)
    h = int(HEIGHT / 2 - R)
    while not found:
        x = random.randint(-w, w)
        y = random.randint(-h, h)
        if not knock({'x': x, 'y': y}, snake):
            bean_pos['x'], bean_pos['y'] = x, y
            found = True


def can_eat():
    return knock(bean_pos, snake[0:1])


def knock_wall():
    head = snake[0]
    return (abs(head['x']) > WIDTH / 2 - R) or (abs(head['y']) > HEIGHT / 2 - R)


def knock_self():
    return knock(snake[0], snake[1:])


'''
functions
'''


def init():
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.penup()

    turtle.onkeypress(up, 'Up')
    turtle.onkeypress(down, 'Down')
    turtle.onkeypress(left, 'Left')
    turtle.onkeypress(right, 'Right')
    turtle.listen()

    for i in range(5):
        snake.append({'x': 0, 'y': -i * 2 * R})

    gen_bean_pos()


def right():
    if speed['x'] == 0:
        speed['x'] = SPEED_VALUE
        speed['y'] = 0


def left():
    if speed['x'] == 0:
        speed['x'] = -SPEED_VALUE
        speed['y'] = 0


def up():
    if speed['y'] == 0:
        speed['x'] = 0
        speed['y'] = SPEED_VALUE


def down():
    if speed['y'] == 0:
        speed['x'] = 0
        speed['y'] = -SPEED_VALUE


def update():
    global eaten, game_over
    # 增加一节
    head = snake[0].copy()
    head['x'] += speed['x']
    head['y'] += speed['y']
    snake.insert(0, head)
    # del snake[-1]  # or snake.pop(-1)

    if eaten:
        gen_bean_pos()
        eaten = False
    else:
        del snake[-1]

    if can_eat():
        eaten = True

    if knock_wall() or knock_self():
        game_over = True


def draw():
    turtle.clear()
    turtle.color('green')
    turtle.goto(bean_pos['x'], bean_pos['y'])
    turtle.dot(2 * R)

    for i, s in enumerate(snake):
        turtle.pencolor(i / len(snake), 0, 0)
        turtle.goto(s['x'], s['y'])  # 移动画笔坐标
        turtle.dot(2 * R)  # 绘制一节蛇
    turtle.update()


def flush():
    update()
    draw()
    if not game_over:
        turtle.ontimer(flush, 100)
    else:
        turtle.home()
        turtle.write('Game Over', align='center', font=('Arial', 40))


init()
flush()

turtle.done()

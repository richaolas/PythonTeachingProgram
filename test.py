import turtle
import random

W = turtle.window_width()
H = turtle.window_height()
R = 15
SPEED = 2 * R
pos = {'x': 0, 'y': 0}
DIR = {'x': 0, 'y': SPEED}
snake = []
direction = {'x': 0, 'y': SPEED}
turtle.tracer(False)
turtle.penup()
game_over = False
turtle.hideturtle()
bean_pos = [0, 0]
eaten = False
score = 0


def gen_bean_pos():
    while True:
        x = random.randint(int(-W / 2 + R), int(W / 2 - R))
        y = random.randint(int(-H / 2 + R), int(H / 2 - R))
        flag = True
        for i in snake:
            x1 = i['x']
            y1 = i['y']
            g = (x1 - x) ** 2 + (y1 - y) ** 2
            if g < SPEED ** 2:
                flag - False
                break
        if flag:
            bean_pos[0], bean_pos[1] = x, y
            break


def can_eat():
    head = snake[0]
    return (head['x'] - bean_pos[0]) ** 2 + (head['y'] - bean_pos[1]) ** 2 < SPEED ** 2


def init():
    for i in range(10):
        x = 0
        y = -i * (2 * R)
        snake.append({'x': x, 'y': y})


def draw():
    turtle.clear()
    # turtle.bgcolor('black')
    turtle.color('green')
    turtle.goto(bean_pos)
    turtle.dot(SPEED)
    turtle.penup()
    turtle.goto(W/2-40,H/2-45)
    turtle.pendown()
    turtle.write(str(score), align='center', font=('Arail', 40))
    cnt = 0
    for s in snake:
        turtle.color(0/255,
                     250/255,
                     154/255)
        cnt += 1
        turtle.goto(s['x'], s['y'])
        turtle.dot(2 * R)
    turtle.update()


def dead():
    head = snake[0]
    x = head['x']
    y = head['y']

    for s in snake[1:]:
        x1 = s['x']
        y1 = s['y']
        dd = (x1 - x) ** 2 + (y1 - y) ** 2
        if dd < SPEED ** 2:
            return True
    if abs(x) > W / 2:
        return True
    if abs(y) > H / 2:
        return True

    return False


def update():
    global game_over
    global eaten
    global score
    head = snake[0].copy()
    head['x'] += DIR['x']
    head['y'] += DIR['y']
    snake.insert(0, head)
    game_over = dead()
    if eaten:
        gen_bean_pos()
        eaten = False
    else:
        del snake[-1]
    if can_eat():
        eaten = True
        score += 10


def flush():
    update()
    draw()

    if not game_over:
        turtle.ontimer(flush, 75)
    else:
        turtle.home()
        turtle.write('Game Over', align='center', font=('Arail', 40))


def left():
    if DIR['x'] == 0:
        DIR['x'] = -SPEED
        DIR['y'] = 0


def right():
    if DIR['x'] == 0:
        DIR['x'] = SPEED
        DIR['y'] = 0


def up():
    if DIR['y'] == 0:
        DIR['x'] = 0
        DIR['y'] = SPEED


def down():
    if DIR['y'] == 0:
        DIR['x'] = 0
        DIR['y'] = -SPEED


init()
flush()

turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')

turtle.listen()

turtle.done()


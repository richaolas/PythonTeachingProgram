import random
import turtle

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
ROLE_R = 20
MOVE = 5
JUMP = 40

game_over = False

ball_coords = []
role_coord = [0, 0]

turtle.hideturtle()
turtle.up()

sprite = turtle.Pen()
sprite.hideturtle()
sprite.up()
sprite.color('red')

turtle.tracer(False)


def collision():
    global game_over
    for b in ball_coords:
        if (b[0] - role_coord[0]) ** 2 + (b[1] - role_coord[1]) ** 2 < (R + ROLE_R) ** 2:
            game_over = True
            break


def draw():
    turtle.clear()
    sprite.clear()
    for ball in ball_coords:
        turtle.goto(ball[0], ball[1])
        turtle.dot(R * 2)
    sprite.goto(role_coord)
    sprite.dot(ROLE_R * 2)
    turtle.update()


def add():
    if random.randint(1, 100) <= 10:
        ball_x = WIDTH / 2 - R
        ball_y = random.randint(-HEIGHT / 2 + R, HEIGHT / 2 - R)
        ball_coords.append([ball_x, ball_y])


def remove():
    global ball_coords
    tmp = []
    for b in ball_coords:
        if not (b[0] < -WIDTH / 2 - R):
            tmp.append(b)
    ball_coords = tmp


def update():
    for b in ball_coords:
        b[0] -= MOVE  # 波点横坐标减小
    role_coord[1] -= MOVE
    add()
    remove()
    collision()


def flush():
    update()
    draw()
    if not game_over:
        turtle.ontimer(flush, 50)
    else:
        turtle.home()
        sprite.write('Game Over', align='center', font=('Arial', 40))


def tap(x, y):
    role_coord[1] += JUMP


flush()
turtle.onscreenclick(tap)
turtle.done()

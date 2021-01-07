import random
import turtle

turtle.up()
turtle.tracer(False)

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
ROLE = 20
MOVE = 5
JUMP = 40

game_over = False

ball_coords = []
role_coord = [0, 0]

sprite = turtle.Pen()
sprite.hideturtle()
sprite.up()
sprite.color('red')


def update():
    for b in ball_coords:
        b[0] -= MOVE  # 波点横坐标减小
    role_coord[1] -= MOVE


def collision():
    global game_over
    for b in ball_coords:
        if (b[0] - role_coord[0]) ** 2 + (b[1] - role_coord[1]) ** 2 < (R + ROLE) ** 2:
            game_over = True
            break


def draw():
    turtle.clear()
    sprite.clear()
    for ball in ball_coords:
        turtle.goto(ball[0], ball[1])
        turtle.dot(R * 2)
    sprite.goto(role_coord)
    sprite.dot(ROLE * 2)
    turtle.update()


def add():
    if random.randrange(20) == 0:
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


def move():
    update()
    add()
    remove()
    collision()
    draw()
    if not game_over:
        turtle.ontimer(move, 50)
    else:
        turtle.home()
        sprite.write('Game Over', align='center', font=('Arial', 40))


def tap(x, y):
    role_coord[1] += JUMP


move()
turtle.onscreenclick(tap)
turtle.done()

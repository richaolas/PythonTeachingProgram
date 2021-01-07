import random
import turtle

turtle.up()
turtle.tracer(False)

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
MOVE = 5

ball_coords = [[0, 0], [100, 100], [200, 200]]

def update():
    for b in ball_coords:
        b[0] -= MOVE # 波点横坐标减小

def draw():
    turtle.clear()
    for ball in ball_coords:
        turtle.goto(ball)
        turtle.dot(R * 2)
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
    draw()
    turtle.ontimer(move, 50)


move()

turtle.done()

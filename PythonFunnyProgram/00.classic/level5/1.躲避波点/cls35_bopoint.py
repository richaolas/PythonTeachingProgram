import random
import turtle

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
SPEED = 5

balls = [[0, 0], [100, 100], [200, 200]]


def add():
    if random.randint(1, 100) <= 10:
        ball_x = WIDTH / 2 - R
        ball_y = random.randint(-HEIGHT / 2 + R, HEIGHT / 2 - R)
        balls.append([ball_x, ball_y])


def remove():
    global balls
    tmp = []
    for ball in balls:
        if abs(ball[0]) <= WIDTH / 2 + R:
            tmp.append(ball)
    balls = tmp


def init():
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.penup()
    turtle.color('red')


def update():
    for ball in balls:
        ball[0] -= SPEED  # 波点横坐标减小
    add()
    remove()


def draw():
    turtle.clear()
    for ball in balls:
        turtle.goto(ball)
        turtle.dot(R * 2)
    turtle.update()


def flush():
    update()
    draw()
    turtle.ontimer(flush, 50)


init()
flush()

turtle.done()

import turtle

turtle.up()
turtle.hideturtle()
turtle.tracer(False)

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
LEVEL = 4
SPEED = 4
JUMP = 50
colors = ('red', 'yellow', 'blue', 'green', 'brown', 'white', 'purple')
balls = []


def init():
    bg = turtle.Pen()
    bg.hideturtle()
    bg.up()

    for i in range(LEVEL):
        x = -WIDTH / 2 + i * WIDTH / LEVEL
        y = HEIGHT / 2

        bg.goto(x, y)
        bg.color(colors[i])
        bg.begin_fill()
        for d in (WIDTH / LEVEL, HEIGHT) * 2:
            bg.forward(d)
            bg.right(90)
        bg.end_fill()

        ball_x = x + (WIDTH / LEVEL / 2)
        ball_y = y - R
        balls.append([ball_x, ball_y])


def update():
    for s in balls:
        s[1] -= SPEED


def draw():
    turtle.clear()
    for s in balls:
        turtle.goto(s[0], s[1])
        turtle.dot(R * 2)
    turtle.update()


def flush():
    update()
    draw()
    turtle.ontimer(flush, 50)


def tap(x, y):
    for i in range(LEVEL):
        # if -WIDTH / 2 + WIDTH / COUNT * i < x < -WIDTH / 2 + WIDTH / COUNT * (i + 1):
        if x < -WIDTH / 2 + WIDTH / LEVEL * (i + 1):
            balls[i][1] += JUMP
            break


init()
flush()
turtle.onscreenclick(tap)

turtle.done()

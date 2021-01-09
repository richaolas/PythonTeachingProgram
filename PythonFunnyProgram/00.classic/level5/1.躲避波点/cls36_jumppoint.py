import turtle

turtle.up()
turtle.hideturtle()
turtle.tracer(False)

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
R = 15
COUNT = 4
DOWN = 4
JUMP = 50

stars = []


def init():
    global stars
    for i in range(COUNT):
        stars.append([-WIDTH / 2 + i * WIDTH / COUNT + WIDTH / COUNT / 2, HEIGHT // 2 - R])
    bg = turtle.Pen()
    bg.hideturtle()
    colors = ['red', 'yellow', 'blue', 'green']
    for i in range(COUNT):
        bg.up()
        bg.goto((-WIDTH / 2 + i * WIDTH / COUNT, HEIGHT / 2))
        bg.color(colors[i])
        bg.begin_fill()
        for d in (WIDTH / COUNT, HEIGHT) * 2:
            bg.forward(d)
            bg.right(90)
        bg.end_fill()


def update():
    for s in stars:
        s[1] -= DOWN


def draw():
    turtle.clear()
    for s in stars:
        turtle.goto(s[0], s[1])
        turtle.dot(R * 2)
    turtle.update()


def flush():
    update()
    draw()
    turtle.ontimer(flush, 50)


def tap(x, y):
    for i in range(COUNT):
        if -WIDTH / 2 + WIDTH / COUNT * i < x < -WIDTH / 2 + WIDTH / COUNT * (i + 1):
            stars[i][1] += JUMP
            break


init()
flush()

turtle.onscreenclick(tap)

turtle.done()

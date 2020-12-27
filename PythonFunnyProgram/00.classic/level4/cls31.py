import turtle

color_pane = {'lt': None, 'padding': 10, 'radius': 25, 'width': None, 'height': None}
colors = ('green', 'red', 'blue', 'yellow', 'black', 'pink')
color_centers = {}

width = turtle.window_width()
height = turtle.window_height()


def init():
    global color_centers

    color_pane['width'] = (color_pane['padding'] + color_pane['radius']) * 2
    color_pane['height'] = (color_pane['padding'] + color_pane['radius'] * 2) * len(colors) + color_pane['padding']

    x = width / 2 - color_pane['padding'] - color_pane['width']
    y = color_pane['height'] / 2
    pos = color_pane['lt'] = (x, y)

    for i in range(len(colors)):
        h = (color_pane['padding'] + color_pane['radius'] * 2) * (i + 1) - color_pane['radius']
        color_centers[colors[i]] = (pos[0] + color_pane['width'] / 2, pos[1] - h)


def jump(pen, pos):
    pen.penup()
    pen.goto(pos)
    pen.pendown()


def draw_color_pane():
    p1 = turtle.Pen()
    p1.hideturtle()
    jump(p1, color_pane['lt'])

    for a in ('width', 'height') * 2:
        p1.fd(color_pane[a])
        p1.right(90)

    for c in colors:
        jump(p1, (color_centers[c][0], color_centers[c][1]))
        p1.dot(color_pane['radius'] * 2, c)


def up():
    p.sety(p.ycor() + 50)
    turtle.update()


def down():
    p.sety(p.ycor() - 50)
    turtle.update()


def left():
    p.setx(p.xcor() - 50)
    turtle.update()


def right():
    p.setx(p.xcor() + 50)
    turtle.update()


def screen_click(x, y):
    for c, center in color_centers.items():
        if (center[0] - x) ** 2 + (center[1] - y) ** 2 <= color_pane['radius'] ** 2:
            p.pencolor(c)
            break
    p.penup()
    p.goto(x, y)
    p.pendown()


drawing = False


def mouse_motion(event):
    global drawing
    if drawing:
        return
    drawing = True  # prevent function be called frequently, then the stack-over flow error
    # if event.state == 264:  # 不同系统和版本这个数字不相同，需要找到状态数字名才行
    p.goto(event.x - width / 2, -event.y + height / 2)
    turtle.update()
    drawing = False


turtle.hideturtle()
turtle.tracer(0, 0)
init()
p = turtle.Pen()
p.hideturtle()
draw_color_pane()

# key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onscreenclick(screen_click)
turtle.listen()

# cv: Canvas 画布
turtle.getscreen().cv.bind("<B1-Motion>", mouse_motion)

turtle.done()

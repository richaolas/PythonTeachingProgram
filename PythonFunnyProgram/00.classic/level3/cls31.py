import turtle
import math
import tkinter

# color_dic = {'green': (300, 140), 'red': (300), 'blue': (___), 'yellow': (___)}

color_pane = {'lt': None, 'padding': 10, 'color_r': 25, 'width':None, 'height':None}
colors = ('green', 'red', 'blue', 'yellow', 'black', 'pink')

color_centers = {}

width = turtle.window_width()
height = turtle.window_height()

def init():
    global color_centers

    color_pane['width'] = color_pane['padding'] * 2 + color_pane['color_r'] * 2
    color_pane['height'] = color_pane['padding'] * (len(colors) + 1) +  color_pane['color_r'] * 2 * len(colors)

    x = width/2 - color_pane['width'] - color_pane['padding']
    y = color_pane['height'] / 2

    pos = color_pane['lt'] = (x, y)
    turtle.goto((pos))
    #pos[0] += (color_pane['padding'] + color_pane['color_r'])
    for i in range(len(colors)):
        #color_centers[colors[i]] = (pos[0] + color_pane['width']/2,
        #            pos[1] - i * (color_pane['padding'] + color_pane['color_r']*2) - color_pane['padding'] - color_pane['color_r'])
        color_centers[colors[i]] = (pos[0] + color_pane['width'] / 2,
                                    pos[1] - color_pane['padding'] - i * (color_pane['color_r'] * 2 + color_pane['padding']) - color_pane['color_r'])



def draw_color_pane():
    p1 = turtle.Pen()
    p1.hideturtle()
    p1.penup()
    p1.goto(color_pane['lt'])
    p1.pendown()
    for i in range(2):
        p1.fd(color_pane['width'])
        p1.right(90)
        p1.fd(color_pane['height'])
        p1.right(90)
    #p1.penup()
    for c in colors:
        p1.penup()
        p1.goto(color_centers[c])
        p1.pendown()
        p1.color(c)
        #p1.pencolor('black')
        p1.setheading(270)
        p1.forward(color_pane['color_r'])
        p1.setheading(0)
        p1.begin_fill()
        p1.circle(color_pane['color_r'])
        p1.end_fill()
        #break


init()


p = turtle.Pen()


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
    
    color = p.pencolor()
    for c, center in color_centers.items():
        if (center[0]-x)**2 + (center[1]-y)**2 < color_pane['color_r']**2:
            color = c
            break
    p.pencolor(color)
    p.penup()
    p.goto(x,y)
    p.pendown()

drawing = False

def mouse_motion(event):
    global drawing
    if drawing:
        return
    drawing = True
    #turtle.getscreen().cv.bind("<Motion>", None)
    #if event.state == 264:  # 不同系统和版本这个数字不相同，需要找到状态数字名才行
    p.goto(event.x - width/2, -event.y + height/2)
    #print(event.state)
    #turtle.
    turtle.update()
    drawing = False
    #pass
    #turtle.getscreen().cv.bind("<Motion>", mouse_motion)

#print(p.pencolor())
turtle.tracer(0,0)
p.hideturtle()
#p.speed(0)
draw_color_pane()
#turtle.tracer(0,0)
turtle.hideturtle()

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onscreenclick(screen_click)
turtle.listen()
#while True:
#    p.goto(0,0)
 #   turtle.update()
turtle.getscreen().cv.bind("<B1-Motion>", mouse_motion)





turtle.done()
-----------------------------------------------
import turtle

color_pane = {'loc': None, 'padding': 10, 'r': 25, 'w': None, 'h': None}
colors = {'red', 'blue', 'yellow', 'black', 'pink', 'green'}

width = turtle.window_width()
height = turtle.window_height()

def init():
    global color_pane
    w = 2 * color_pane['padding'] + 2 * color_pane['r']
    color_pane['w'] = w
    h = 2 * len(colors) * color_pane['r'] + (len(colors) + 1) * color_pane['padding']
    color_pane['h'] = h
    x = width / 2 - w - color_pane['padding']
    y = h / 2
    color_pane['loc'] = (x, y)

def draw_color_pane():
    turtle.penup()
    turtle.goto(color_pane['loc'])
    turtle.pendown()

    for i in range(2):
        turtle.forward(color_pane['w'])
        turtle.right(90)
        turtle.forward(color_pane['h'])
        turtle.right(90)

init()
draw_color_pane()

turtle.done()

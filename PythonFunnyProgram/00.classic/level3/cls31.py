import turtle
import math

# color_dic = {'green': (300, 140), 'red': (300), 'blue': (___), 'yellow': (___)}

color_pane = {'lt': (300, 200), 'padding': 10, 'color_r': 25}
colors = ('green', 'red', 'blue', 'yellow')

color_centers = {}

width = turtle.window_width()
height = turtle.window_height()

def init():
    global color_centers
    pos = color_pane['lt']
    #pos[0] += (color_pane['padding'] + color_pane['color_r'])
    for i in range(len(colors)):
        color_centers[colors[i]] = (pos[0] + color_pane['padding'] + color_pane['color_r'],
                    pos[1] - i * (color_pane['padding'] + color_pane['color_r']*2) - color_pane['padding'] - color_pane['color_r'])



def draw_color_pane():
    p1 = turtle.Pen()
    p1.hideturtle()
    p1.penup()
    p1.goto(color_pane['lt'])
    p1.pendown()
    for i in range(2):
        p1.fd((color_pane['padding'] + color_pane['color_r'])*2)
        p1.right(90)
        p1.fd(color_pane['padding'] * 5 + color_pane['color_r']*8)
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
    if event.state == 264:
        p.goto(event.x - width/2, -event.y + height/2)
    print(event)
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
#while True:
#    p.goto(0,0)
 #   turtle.update()
turtle.getscreen().cv.bind("<Motion>", mouse_motion)
turtle.listen()




turtle.done()

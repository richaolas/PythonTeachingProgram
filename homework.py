import turtle


R=15
SPEED=2*R
pos={'x':0,'y':0}
DIR={'x':0,'y':SPEED}
snake=[]
direction={'x':0,'y':SPEED}
turtle.tracer(False)
turtle.penup()
game_over=False

def init():
    for i in range(5):
        x=0
        y=-i*(2*R)
        snake.append({'x':x,'y':y})



def draw():
    turtle.clear()
    for s in snake:
        turtle.goto(s['x'],s['y'])
        turtle.dot(2*R)
    turtle.update()
def dead():
    head=snake[0]
    x=head['x']
    y=head['y']

    for s in snake[1:]:
        x1=s['x']
        y1=s['y']
        dd=(x1-x)**2+(y1-y)**2
        if dd<SPEED**2:
            return True
    return False
def update():

    global game_over
    head=snake[0].copy()
    head['x']+=DIR['x']
    head['y'] +=DIR['y']

def flush():
    update()
    draw()
    turtle.ontimer(flush,100)
    if not game_over:
        turtle.ontimer(flush,100)
    else:
        turtle.home()
        turtle.write('Game Over',align='center',font=('Arail',40))


def left():
    DIR['x']=-SPEED
    DIR['y']=0
def right():
    DIR['x']=SPEED
    DIR['y']=0
def up():
    DIR['x']=0
    DIR['y']=SPEED
def down():
    DIR['x']=0
    DIR['y']=-SPEED



init()
flush()


turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
turtle.onkeypress(up,'Up')
turtle.onkeypress(down,'Down')


turtle.listen()




turtle.done()




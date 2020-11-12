import turtle

t = turtle.Turtle()


def setpen(x, y):
    # 抬笔
    t.penup()
    # 移动画笔到(x, y)
    t.goto(x, y)
    # 落笔
    t.pendown()
    t.setheading(0)


def circle(x, y, r, color):
    # 起始位置
    start_x = x
    start_y = y - r
    # 移动画笔
    setpen(start_x, start_y)
    # 选择画笔颜色
    t.pencolor(color)
    # 选择背景色
    t.fillcolor(color)
    # 填充
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def five_star(l):
    setpen(0, 0)
    t.setheading(162)
    t.forward(150)
    t.setheading(0)
    t.fillcolor('WhiteSmoke')
    t.begin_fill()
    t.hideturtle()
    t.penup()  ## 技巧：penup 的时候可以进行 fill，可以理解为 penup 绘制了一个区域
    for i in range(5):
        t.forward(l)
        t.right(144)
    t.end_fill()


def sheild():
    circle(0, 0, 300, 'red')
    circle(0, 0, 250, 'white')
    circle(0, 0, 200, 'red')
    circle(0, 0, 150, 'blue')
    five_star(284) # 1.9 * 150


if __name__ == '__main__':
    sheild()
    # 结束乌龟图
    turtle.done()

from turtle import *

def nose(x, y):
    """画鼻子"""
    pensize(5)
    pencolor((255, 155, 192))
    penup()
    # 将海龟移动到指定的坐标
    goto(x, y)
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    fillcolor(255, 192, 203)
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x, y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(90)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x, y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x, y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def body(x, y):
    '''画身体'''
    penup()
    goto(x, y)
    pencolor('red')
    fillcolor(250, 106, 106)
    pendown()
    begin_fill()
    setheading(-66)
    circle(-450, 17)
    setheading(180)
    forward(185)
    setheading(85)
    circle(-450, 17)
    end_fill()
    '''右手'''
    penup()
    goto(110, -45)
    pendown()
    pensize(8)
    pencolor(255, 192, 203)
    setheading(30)
    circle(-400, 10)
    penup()
    goto(167, -5)
    pendown()
    setheading(-120)
    forward(20)
    left(100)
    forward(20)
    '''左手'''
    penup()
    goto(-25, -45)
    pendown()
    pencolor(255, 192, 203)
    setheading(150)
    circle(400, 10)
    penup()
    goto(-78, -6)
    pendown()
    setheading(-60)
    forward(20)
    right(100)
    forward(20)


def feet1(x, y):
    pensize(7)
    pencolor(255, 192, 203)
    penup()
    goto(x, y)
    setheading(-90)
    pendown()
    forward(10)
    penup()
    goto(x - 12, y - 10)
    pendown()
    pencolor(238, 201, 0)
    fillcolor(238, 230, 132)
    begin_fill()
    setheading(0)
    forward(24)
    right(90)
    forward(36)
    right(90)
    forward(40)
    circle(-10, 180)
    forward(16)
    left(90)
    forward(12)
    end_fill()


def feet2(x, y):
    pensize(7)
    pencolor(255, 192, 203)
    penup()
    goto(x, y)
    setheading(-90)
    pendown()
    forward(10)
    penup()
    goto(x - 12, y - 10)
    pendown()
    pencolor(238, 201, 0)
    fillcolor(238, 230, 132)
    begin_fill()
    setheading(0)
    forward(24)
    right(90)
    forward(36)
    right(90)
    forward(40)
    circle(-10, 180)
    forward(16)
    left(90)
    forward(12)
    end_fill()


def tail(x, y):
    pensize(8)
    penup()
    goto(x, y)
    pendown()
    pencolor(255, 192, 203)
    setheading(-5)
    circle(30, 100)
    circle(10, 180)
    circle(20, 150)


def backg(x):
    penup()
    goto(-420, x)
    setheading(0)
    fillcolor(50, 205, 50)
    begin_fill()
    forward(840)
    right(90)
    forward(300)
    right(90)
    forward(840)
    right(90)
    forward(300)
    end_fill()
    setheading(0)
    fillcolor(0, 191, 255)
    begin_fill()
    forward(840)
    left(90)
    forward(600)
    left(90)
    forward(840)
    left(90)
    forward(600)
    end_fill()


def cloude1(x, y):
    """画云"""
    penup()
    goto(x, y)
    setheading(90)
    fillcolor(255, 255, 255)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.14
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.15
            left(3)
            forward(a)
    end_fill()


def cloude2(x, y):
    """画云"""
    penup()
    goto(x, y)
    setheading(90)
    fillcolor(255, 255, 255)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.15
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.13
            left(3)
            forward(a)
    end_fill()


def setting():
    """设置参数"""
    pensize(5)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 700)
    speed(10)


def main():
    """主函数"""

    setting()
    backg(0)
    body(105, -20)
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    feet1(10, -150)
    feet2(90, -150)
    tail(130, -110)
    cloude1(-200, 200)
    cloude2(300, 300)
    done()


if __name__ == '__main__':
    main()
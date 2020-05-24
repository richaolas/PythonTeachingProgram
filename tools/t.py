import turtle, time
#
#
# class DCS():
#     '''绘制自定义笛卡尔平面直角坐标系。
#     \npen：画笔； x_v：x轴量程； y_v：y轴量程； x_dk：x轴大刻度度量； y_dk：y轴大刻度度量
#     \nquadrant：绘制坐标系包含的象限，默认为'1234'，即一二三四象限；
#     \nallk：横轴和纵轴上每个大刻度之间，用来绘制小刻度将此区间划分为多个最小区间，默认为allk=2
#     \nX：横轴标注，默认‘X’； Y：纵轴标准，默认‘Y’； O：原点标注，默认‘O’
#     \nk：等于True时，自动生成坐标系。等于False时，则不生成。
#     \n### author：peipei12138 (CSDN) ###
#     \n### 最后修改于：2020/4/25 21:52 ###'''
#
#     def __init__(self, pen, x_v, y_v, x_dk, y_dk, quadrant='1234', allk=2, X='X', Y='Y', O='O', k=True):
#
#         self.pen = pen
#         self.x_v = abs(x_v)
#         self.y_v = abs(y_v)
#         self.x_dk = x_dk
#         self.y_dk = y_dk
#         self.allk = allk
#         self.quadrant = "".join(sorted(list(set(quadrant))))
#
#         if k == True:
#             self.pen.ht()
#             self.pen.speed(10)
#             self.x_y(X, Y, O)  # 绘制坐标系框架
#             self.bigscale()  # 绘制大刻度
#
#             self.pen.speed(5)
#             self.pen.pensize(2)
#
#     def x_y(self, X='X', Y='Y', O='O'):
#         '''绘制 坐标系 框架'''
#         self.pen.pensize(2)
#         self.pen.up()
#
#         GO = self.pen.goto
#         dd = self.d
#         UP = self.pen.up
#         DW = self.pen.down
#         WT = self.pen.write
#
#         def _x(x, kh=True):
#             '''绘制横轴'''
#             GO(dd(0, 0))
#             DW()
#             GO(dd(x + 5, 0));
#             UP()
#             if kh == True:
#                 DW();
#                 GO(dd(x, 5));
#                 GO(dd(x + 5, 0));
#                 GO(dd(x, -5));
#                 UP()
#                 GO(dd(x + 10, -10));
#                 WT(X)
#
#         def _y(y, kh=True):
#             '''绘制纵轴'''
#             GO(dd(0, 0))
#             DW()
#             GO(dd(0, y + 5));
#             UP()
#             if kh == True:
#                 DW();
#                 GO(dd(5, y));
#                 GO(dd(0, y + 5));
#                 GO(dd(-5, y));
#                 UP()
#                 GO(dd(-10, y + 7));
#                 WT(Y)
#
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13']:  # 原点在画布中点
#             GO(dd(-15, -20));
#             WT(O)
#             _x(305)
#             _y(305)
#
#             _x(-315, False)
#             _y(-315, False)
#
#         elif self.quadrant == '1':  # 原点在左下角
#             GO(dd(-15, -20));
#             WT(O)
#             _x(605)
#             _y(605)
#
#         elif self.quadrant == '2':  # 原点在右下角
#             GO(dd(2, -20));
#             WT(O)
#             _x(15)
#             _y(605)
#
#             _x(-615, False)
#             _y(-25, False)
#
#         elif self.quadrant == '3':  # 原点在右上角
#             GO(dd(5, 10));
#             WT(O)
#             _x(15)
#             _y(15)
#
#             _x(-615, False)
#             _y(-615, False)
#
#         elif self.quadrant == '4':  # 原点在左上角
#             GO(dd(-10, -15));
#             WT(O)
#             _x(605)
#             _y(15)
#
#             _x(-25, False)
#             _y(-615, False)
#
#         elif self.quadrant in ['12', '34']:  # 原点在中上方或中下方
#             if self.quadrant == '12':
#                 GO(dd(0, -15));
#                 WT(O)
#                 _y(605)
#                 _y(-25, False)
#             else:
#                 GO(dd(10, 5));
#                 WT(O)
#                 _y(-615, False)
#                 _y(15)
#
#             _x(305)
#             _x(-315, False)
#
#         elif self.quadrant in ['14', '23']:  # 原点在左中部或右中部
#             if self.quadrant == '14':
#                 GO(dd(-10, -15));
#                 WT(O)
#                 _x(605)
#                 _x(-25, False)
#             else:
#                 GO(dd(5, -15));
#                 WT(O)
#                 _x(-615, False)
#                 _x(15)
#
#             _y(305)
#             _y(-315, False)
#
#     def bigscale(self):
#         '''绘制有数量标记的大刻度'''
#         self.pen.up()
#
#         GO = self.pen.goto
#         DD = self.D
#         UP = self.pen.up
#         DW = self.pen.down
#         WT = self.pen.write
#
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13', '12', '34']:
#             xlong = 300
#         if self.quadrant in ['1', '2', '3', '4', '14', '23']:
#             xlong = 600
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13', '23', '14']:
#             ylong = 300
#         if self.quadrant in ['1', '2', '3', '4', '12', '34']:
#             ylong = 600
#
#         def _x(f=1):
#             ''''''
#             self.pen.pensize(2)
#
#             xdk = f * self.x_dk
#             xv = f * int(self.x_v / self.x_dk) * self.x_dk
#
#             xadd = xdk
#             while abs(xadd) <= abs(xv):
#                 GO(DD(xadd, 5 * (self.y_v / ylong)));
#                 DW();
#                 GO(DD(xadd, -5 * (self.y_v / ylong)));
#                 UP()
#                 xadd += xdk
#             # for xadd in range(min(xdk, xv), max(xdk, xv) + 1, self.x_dk):
#             #    GO(DD(xadd, 5 * (self.y_v / ylong)));DW();GO(DD(xadd, -5 * (self.y_v/ylong)));UP()
#
#         def _y(f=1):
#             ''''''
#             self.pen.pensize(2)
#
#             ydk = f * self.y_dk
#             yv = f * int(self.y_v / self.y_dk) * self.y_dk
#
#             yadd = ydk
#             while abs(yadd) <= abs(yv):
#                 GO(DD(5 * (self.x_v / xlong), yadd));
#                 DW();
#                 GO(DD(-5 * (self.x_v / xlong), yadd));
#                 UP()
#                 yadd += ydk
#             # for yadd in range(min(ydk, yv), max(ydk, yv) + 1, self.y_dk):
#             #    GO(DD(5 * (self.x_v / xlong), yadd));DW();GO(DD(-5 * (self.x_v / xlong), yadd));UP()
#
#         def rc_x(l=1, f=1):
#             '''消除横轴半边刻度
#             \nl=1：消除横轴上方；l=-1：消除横轴下方
#             \nf=1：消除纵轴右边；f=-1：消除纵轴左边'''
#             self.pen.pensize(5)
#
#             if l == 1:
#                 rm = 17
#             elif l == -1:
#                 rm = 5.4
#
#             xdk = f * self.x_dk
#             xv = f * int(self.x_v / self.x_dk) * self.x_dk
#
#             self.pen.pencolor('white')
#             GO(DD(xdk / self.allk, 4 * l * (self.y_v / ylong)));
#             DW();
#             GO(DD(xv, 4 * l * (self.y_v / ylong)));
#             UP()
#             self.pen.pencolor('black')
#
#             # 标上刻度读数
#             xadd = xdk
#             while abs(xadd) <= abs(xv):
#                 GO(DD(xadd, - rm * l * (self.y_v / ylong)));
#                 WT(f'{str(round(xadd, 10))}')
#                 xadd += xdk
#             # for xadd in range(min(xdk, xv), max(xdk, xv) + 1, self.x_dk):
#             #    GO(DD(xadd, - rm * l * (self.y_v / ylong)));WT(f'{str(xadd)}')
#
#         def rc_y(l=1, f=1):
#             '''消除纵轴半边刻度
#             \nl=1：消除纵轴右边；l=-1：消除纵轴左边
#             \nf=1：消除横轴上方；f=-1：消除横轴下方'''
#             self.pen.pensize(5)
#
#             if l == 1:
#                 rm = 15 + max(len(str(-self.y_dk)), len(str(-self.y_v))) * 2
#             elif l == -1:
#                 rm = 5
#
#             ydk = f * self.y_dk
#             yv = f * int(self.y_v / self.y_dk) * self.y_dk
#
#             self.pen.pencolor('white')
#             GO(DD(4 * l * (self.x_v / xlong), ydk / self.allk));
#             DW();
#             GO(DD(4 * l * (self.x_v / xlong), yv));
#             UP()
#             self.pen.pencolor('black')
#
#             # 标上刻度读数
#             yadd = ydk
#             while abs(yadd) <= abs(yv):
#                 GO(DD(- rm * l * (self.x_v / xlong), yadd));
#                 WT(f'{str(round(yadd, 10))}')
#                 yadd += ydk
#             # for yadd in range(min(ydk, yv), max(ydk, yv) + 1, self.y_dk):
#             #    GO(DD(- rm * l * (self.x_v / xlong), yadd));WT(f'{str(yadd)}')
#
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13']:
#             # 横轴正半轴
#             _x(1)
#             self.smallscale('x', 1)
#             rc_x(1, 1)
#             # 纵轴正半轴
#             _y(1)
#             self.smallscale('y', 1)
#             rc_y(1, 1)
#             # 横轴负半轴
#             _x(-1)
#             self.smallscale('x', -1)
#             rc_x(1, -1)
#             # 纵轴负半轴
#             _y(-1)
#             self.smallscale('y', -1)
#             rc_y(1, -1)
#
#         elif self.quadrant == '1':
#             # 横轴正半轴
#             _x(1)
#             self.smallscale('x', 1)
#             rc_x(1, 1)
#             # 纵轴正半轴
#             _y(1)
#             self.smallscale('y', 1)
#             rc_y(1, 1)
#
#         elif self.quadrant == '2':
#             # 横轴负半轴
#             _x(-1)
#             self.smallscale('x', -1)
#             rc_x(1, -1)
#             # 纵轴正半轴
#             _y(1)
#             self.smallscale('y', 1)
#             rc_y(-1, 1)
#
#         elif self.quadrant == '3':
#             # 横轴负半轴
#             _x(-1)
#             self.smallscale('x', -1)
#             rc_x(-1, -1)
#             # 纵轴负半轴
#             _y(-1)
#             self.smallscale('y', -1)
#             rc_y(-1, -1)
#
#         elif self.quadrant == '4':
#             # 横轴正半轴
#             _x(1)
#             self.smallscale('x', 1)
#             rc_x(-1, 1)
#             # 纵轴负半轴
#             _y(-1)
#             self.smallscale('y', -1)
#             rc_y(1, -1)
#
#         elif self.quadrant in ['12', '34']:
#             # 横轴正负半轴
#             _x(1)
#             self.smallscale('x', 1)
#             _x(-1)
#             self.smallscale('x', -1)
#             if self.quadrant == '12':
#                 rc_x(1, 1)
#                 rc_x(1, -1)
#                 # 纵轴正半轴
#                 _y(1)
#                 self.smallscale('y', 1)
#                 rc_y(1, 1)
#
#             else:
#                 rc_x(-1, 1)
#                 rc_x(-1, -1)
#                 # 纵轴负半轴
#                 _y(-1)
#                 self.smallscale('y', -1)
#                 rc_y(1, -1)
#
#         elif self.quadrant in ['14', '23']:
#             # 纵轴正负半轴
#             _y(1)
#             self.smallscale('y', 1)
#             _y(-1)
#             self.smallscale('y', -1)
#             if self.quadrant == '14':
#                 rc_y(1, 1)
#                 rc_y(1, -1)
#                 # 横轴正半轴
#                 _x(1)
#                 self.smallscale('x', 1)
#                 rc_x(1, 1)
#
#             else:
#                 rc_y(-1, 1)
#                 rc_y(-1, -1)
#                 # 横轴负半轴
#                 _x(-1)
#                 self.smallscale('x', -1)
#                 rc_x(1, -1)
#
#     def smallscale(self, a, f):
#         '''绘制最小刻度标识'''
#         dictdk = {'x': self.x_dk, 'y': self.y_dk}
#         dictv = {'x': self.x_v, 'y': self.y_v}
#
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13', '12', '34']:
#             xlong = 300
#         if self.quadrant in ['1', '2', '3', '4', '14', '23']:
#             xlong = 600
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13', '23', '14']:
#             ylong = 300
#         if self.quadrant in ['1', '2', '3', '4', '12', '34']:
#             ylong = 600
#
#         if self.allk == 1:
#             return
#         self.pen.pensize(1)
#         self.pen.up()
#
#         dk = f * dictdk[a] / self.allk
#         v = f * int(dictv[a] / dk) * dk
#
#         add = dk
#
#         while abs(add) < abs(v):
#             if a == 'x':
#                 self.pen.goto(self.D(add, 2.5 * (self.y_v / ylong)))
#                 self.pen.down()
#                 self.pen.goto(self.D(add, - 2.5 * (self.y_v / ylong)))
#                 self.pen.up()
#             if a == 'y':
#                 self.pen.goto(self.D(2 * (self.x_v / xlong), add))
#                 self.pen.down()
#                 self.pen.goto(self.D(- 4 * (self.x_v / xlong), add))
#                 self.pen.up()
#
#             add += dk
#
#     def D(self, x, y):
#         '''改变 画布 坐标系统 为 自定义 坐标系 的 坐标系统'''
#         l1 = 300
#         l2 = 600
#
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13']:
#             return x * (l1 / self.x_v), y * (l1 / self.y_v)
#
#         elif self.quadrant in ['1', '2', '3', '4']:
#             q = self.quadrant
#             rx = x * (l2 / self.x_v)
#             ry = y * (l2 / self.y_v)
#             if q == '1':
#                 return rx - l1, ry - l1
#             elif q == '2':
#                 return rx + l1, ry - l1
#             elif q == '3':
#                 return rx + l1, ry + l1
#             else:
#                 return rx - l1, ry + l1
#
#         elif self.quadrant in ['12', '34']:
#             q = self.quadrant
#             rx = x * (l1 / self.x_v)
#             ry = y * (l2 / self.y_v)
#             if q == '12':
#                 return rx, ry - l1
#             else:
#                 return rx, ry + l1
#
#         elif self.quadrant in ['23', '14']:
#             q = self.quadrant
#             rx = x * (l2 / self.x_v)
#             ry = y * (l1 / self.y_v)
#             if q == '23':
#                 return rx + l1, ry
#             else:
#                 return rx - l1, ry
#
#     def d(self, x, y):
#         '''改变 画布 坐标原点 到 画布合适 地方'''
#         if self.quadrant in ['1234', '123', '134', '124', '234', '24', '13']:
#             return x, y
#
#         elif self.quadrant in ['1', '2', '3', '4']:
#             q = self.quadrant
#             rx = x
#             ry = y
#             if q == '1':
#                 return rx - 300, ry - 300
#             elif q == '2':
#                 return rx + 300, ry - 300
#             elif q == '3':
#                 return rx + 300, ry + 300
#             else:
#                 return rx - 300, ry + 300
#
#         elif self.quadrant in ['12', '34']:
#             q = self.quadrant
#             rx = x
#             ry = y
#             if q == '12':
#                 return rx, ry - 300
#             else:
#                 return rx, ry + 300
#
#         elif self.quadrant in ['23', '14']:
#             q = self.quadrant
#             rx = x
#             ry = y
#             if q == '23':
#                 return rx + 300, ry
#             else:
#                 return rx - 300, ry


width, height = turtle.window_width(), turtle.window_height()
print(width, height)
turtle.hideturtle()


def arrow(size=10, angle=45):
    heading = turtle.heading()
    turtle.left(180-angle)
    turtle.forward(size)
    turtle.backward(size)
    turtle.setheading(heading)
    turtle.right(180 - angle)
    turtle.forward(size)
    turtle.backward(size)
    turtle.setheading(heading)

turtle.arrow = arrow

if __name__ == "__main__":
    turtle.penup()
    turtle.goto(-width/2, 0)
    turtle.pendown()
    turtle.goto(width/2,0)
    turtle.arrow()
    # t = turtle.Pen()
    # t.up()
    # p = DCS(t, 15, 15, 3, 3, '14', 3)
    # t.goto(p.D(0, 0))
    # t.pencolor('red')
    # t.down()
    # t.goto(p.D(10.5, 12))

    #time.sleep(6)
    turtle.done()

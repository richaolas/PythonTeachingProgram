# # 题目一
# friend1 = input('input friend')
# friend2 = input('input other friend')
#
# print(friend1 + ' and ' + friend2 + ' are friends.')

# 题目二
import turtle

#根据输入边数，画多边形
n = int(input('how many edges? '))
color = input('input color which you like?: ')

turtle.fillcolor(color)
turtle.begin_fill()
for i in range(1, n + 1):
    turtle.forward(50)
    turtle.left(360 / n)
turtle.end_fill()

turtle.done()


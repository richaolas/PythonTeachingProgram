import turtle

#根据输入边数，画多边形
n = int(input('how many edges? '))

for i in range(1, n + 1):
    turtle.forward(50)
    turtle.left(360 / n)

turtle.done()

#输入姓名，打招呼
name = input('please input your name: ')
print('Hello ' + name)

#输入两个数字，求数字的和
a = input('please input first number: ')
b = input('please input second number: ')
print(int(a) + int(b))

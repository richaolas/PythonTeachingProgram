num1 = input('请输入数字：')
num2 = input('请输入数字：')
num3 = input('请输入数字：')
sym1 = input('请输入符号：')
sym2 = input('请输入符号：')

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

if sym1 == '+' and sym2 == '-':
    print(num1+num2-num3)
elif sym1 == '-' and sym2 == '+':
    print(num1-num2+num3)
elif sym1 == '*' and sym2 == '/':
    print(num1*num2/num3)
elif sym1 == '/' and sym2 == '*':
    print(num1/num2*num3)
elif sym1 == '+' and sym2 == '*':
    print(num1+num2*num3)
elif sym1 == '*' and sym2 == '+':
    print(num1*num2+num3)
elif sym1 == '+' and sym2 == '/':
    print(num1+num2/num3)
elif sym1 == '/' and sym2 == '+':
    print(num1/num2+num3)
elif sym1 == '-' and sym2 == '*':
    print(num1-num2*num3)
elif sym1 == '*' and sym2 == '-':
    print(num1*num2-num3)
elif sym1 == '-' and sym2 == '/':
    print(num1-num2/num3)
elif sym1 == '/' and sym2 == '-':
    print(num1/num2-num3)
else:
    print("错误的运算符号")
    
import turtle
turtle.onkey()


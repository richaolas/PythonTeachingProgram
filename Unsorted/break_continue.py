# 判断一个数字（>2）是不是素数
n = int(input('input number'))
flag = True
for i in range(2, n):
    if n % i == 0:
        flag = False
        break #结束整个循环
if flag:
    print('Yes')
else:
    print('NO')


n = int(input('input number'))
for i in range(2, n):
    if n % i == 0:
        print('NO')
        break #结束整个循环
else:
    print('Yes')

# 0-100 所有，不能被3，or 5，or 7整除的数，要求
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        continue #结束一次循环，进入到下一次循环
    print(i, end=' ')

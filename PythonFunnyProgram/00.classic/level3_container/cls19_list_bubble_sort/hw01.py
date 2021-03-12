'''
向一个列表中添加任意50个元素，写一个程序，要求把奇数放在前面，偶数放在后面（不要求按照大小顺序排序）。例如 a = [1,4,5,2,3] 经过计算后得到 a = [1,5,3,4,2]
'''

import random

a = []

for i in range(50):
    a.append(random.randint(1,100))

print(a)

for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] % 2 == 0 and a[j + 1] % 2 == 1:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)


# -*- coding: utf-8 -*-
import os

i = 1
while i <= 9:
    j = 1
    while j < i+1:
        print("%d*%d=%d "%(j,i,j*i), end = '')
        j += 1
    print("\n",end='')
    i += 1
# os.system("pause")

#计算1到100的累加和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("累加和：",sum)

#计算1到100的累乘积
i = 1
mul = 1
while i <= 100:
    mul *= i
    i += 1
print("累乘积：",mul)
print("长度：",len(str(mul)))
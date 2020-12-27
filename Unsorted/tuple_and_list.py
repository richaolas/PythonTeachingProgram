import random

li = []

for i in range(10):
    li.append(random.randint(0, 10))

print('Before add 1:')
print(li)

for i in range(len(li)):
    li[i] += 1

print('After add 1:')
print(li)

for item in li:
    item += 1

print('After add 1:')
print(li)

t = (1,2,3)
t[0] = 0 #元组是不可变对象，不能修改元组的内容 TypeError: 'tuple' object does not support item assignment
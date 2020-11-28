# import turtle
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
#
# x.update(y)
#
# print(x)
#
# # turtle.write('Jerry', font='fontsize=18')
# # turtle.forward(300)
# # turtle.goto(0,-100)
# # turtle.write('Bruce', font='fontsize=18')
#
# #turtle.done()


import random
n = [random.randint(1, 9)]
for i in range(9):
    n.append(random.randint(0, 9))
print(n)
# n = [9] * 10

n[9] += 1
for i in range(9):
    if n[9 - i] >= 10:
        n[9 - i] = n[9 - i] - 10
        n[8 - i] += 1
if n[0] >= 10:
    n[0] -= 10
    n.insert(0, 1)
print(n)
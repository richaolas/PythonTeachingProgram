"""
随机生成两个含有10个整型元素的列表，然后利用for循环讲两个列表中的元素交叉合并：
例如 a = [1,2,3,4] b = [5,6,7,8] 结果 c = [1,5,2,6,3,7,4,8]
"""

import random

list1 = []
list2 = []
for i in range(10):
    list1.append(random.randint(1, 100))
    list2.append(random.randint(1, 100))
print('list1:', list1)
print('list2:', list2)
# zhangyuchi
# t = 1
# for s in range(10):
#     list1.insert(s + t,list2[s])
#     t += 1
# ric
for i in range(len(list2)):
    list1.insert(i * 2 + 1, list2[i])

print('list1 + list2:', list1)

# 1. 最多的
# 2，按条件
# 3. index
# 4. all index


import random

a = []
n = 20
for i in range(n):
    a.append(random.randint(1,10))

print(a)

idxs = []
start = 0

while True:
    try:
        start = a.index(1, start, len(a))
        idxs.append(start)
        start += 1
    except ValueError as e:
        print(e, type(e))
        break

print(idxs, a.count(1))

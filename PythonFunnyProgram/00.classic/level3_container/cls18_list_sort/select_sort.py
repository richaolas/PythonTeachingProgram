import random

n = 10

a = []
for i in range(n):
    a.append(random.randint(1, 100))

print(a)

for i in range(n-1):
    k = 0
    m = a[0]
    for j in range(n-i):
        if a[j] > m:
            m = a[j]
            k = j
    a[n-i-1], a[k] = a[k], a[n-i-1]

print(a)


# QA:
# 1. how to check whether the list is sorted?

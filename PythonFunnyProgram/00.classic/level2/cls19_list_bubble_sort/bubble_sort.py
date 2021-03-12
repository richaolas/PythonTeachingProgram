import random

n = 10

a = []
for i in range(n):
    a.append(random.randint(1, 100))


def bubble_sort(c):
    for i in range(len(c)):
        for j in range(len(c) - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]


bubble_sort(a)
print(a)

# QA:
# 1. how to check whether the list is sorted?

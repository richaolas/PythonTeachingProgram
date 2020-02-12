k = int(input())

a, b = 1, 1

for i in range(1, k):
    a, b = b, a + b

print(a)


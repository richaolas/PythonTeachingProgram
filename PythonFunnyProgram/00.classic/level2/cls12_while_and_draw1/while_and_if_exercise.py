# 获取1-99 5出现的次数

n = 1
c = 0

while n < 100:
    if n // 10 == 5:
        c = c + 1
    if n % 10 == 5:
        c = c + 1
    n = n + 1

print(c)

# 计算 m 的 n 次幂

m = 5
n = 10

a = 1
result = 1
while a <= n:
    result = result * m
    a = a + 1

print(result)

# 计算斐波那契数列

a, b = 1, 1
n = 1
print(a, b, end=' ')
while n <= 10:
    a, b = b, a + b
    print(b, end=' ')
    n = n + 1

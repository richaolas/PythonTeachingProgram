a = int(input('input a number: '))
b = int(input('input a number: '))
# format : a + b = c
print(str(a) + ' + ' + str(b) + ' = ' + str(a+b))
print('%d + %d = %d' % (a, b, a+b))

for row in range(1, 10):
    for i in range(1, row + 1):  # 1, 2, ... row
        print('%d*%d=%d' % (i, row, i * row), end=' ')
    print()

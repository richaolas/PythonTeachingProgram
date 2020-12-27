a,b,c = map(int, input().strip().split(' '))

for x in range(c//a+1):
    for y in range((c-a*x)//b+1):
        if a * x + b * y == c:
            print('%d x %d + %d x %d = %d' % (a, x, b, y, c))

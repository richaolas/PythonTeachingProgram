def printTriangle():
    print('   *    ')
    print('  ***   ')
    print(' ****** ')
    return 1, 3, 5


a, b, c = printTriangle()
print(a, b, c)

n = 100

def a(x):
    global n  # local
    n = 200
    return x + 5


def b(x):
    n = 300
    return x * 0.7

print(n)
a(1)
print(n)
b(1)
print(n)

def f():
    def g():
        print('I am a inner function')
    g()
    return g


innerg = f()
innerg()

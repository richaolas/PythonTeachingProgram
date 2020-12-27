def f(n):
    if n in [0, 1]:
        return 1
    return f(n-1) + f(n-2)


def f2(n):
    if n in [0, 1]:
        return 1
    if n == 2:
        return 2
    return f(n-1) + f(n-2) + f(n-3)


def g(n):
    if n == 0:
        return 1
    return n * g(n - 1)


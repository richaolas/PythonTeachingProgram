import time


def timertest(func):
    def wrapped(*args, **kwargs):
        beg = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('%s cost %s' % (func.__name__, str(end - beg)))

    return wrapped


@timertest  # fun1 = timertest(fun1)
def fun1(a, b):
    print(a, b)
    time.sleep(1)


@timertest  # fun2 = timertest(fun2)
def fun2(a, b, c):
    print(a, b, c)
    time.sleep(1)


fun1(1, 2)
fun2(1, 2, 3)

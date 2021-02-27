from functools import reduce

a = [1,2,3,4,5]

b = reduce(lambda x,y:x+y, a, 10)

print(b)

def reduce2(f, c, init):
    for i in c:
        init = f(init, i)
    return init

b = reduce2(lambda x,y:x+y, a, 10)

print(b)
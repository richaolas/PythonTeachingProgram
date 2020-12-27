def factorSum(n):
    return sum([i for i in range(1,n) if n % i == 0])

def getQinHeNumber(a):
    b = factorSum(a)
    if a != b:
        tmp = factorSum(b)
        if tmp == a:
            return True, a, b
    return False, None, None

n = 1
while True:
    ret, a, b = getQinHeNumber(n)
    if ret:
        print(a, b)
        break
    n += 1

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def GoldbachSolution(n):
    for i in range(2, n):
        if isprime(i) and isprime(n - i):
            return i, n - i

for n in range(6, 100+1, 2):
    a,b = GoldbachSolution(n)
    print('%d=%d+%d'%(n,a,b))

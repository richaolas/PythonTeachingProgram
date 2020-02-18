
def Hanoi(n, fromTower, midTower, toTower):
    if n == 1:
        print('%s-->%s' % (fromTower, toTower))
    else:
        Hanoi(n-1, fromTower, toTower, midTower)
        print('%s-->%s' % (fromTower, toTower))
        Hanoi(n-1, midTower, fromTower, toTower)

Hanoi(2, 'A', 'B', 'C')

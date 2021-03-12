import random

n = random.randint(1, 25)
for i in range(5):
    num = int(input('你有五次回答机会：(%d/5): ' % (i + 1)))
    if num > n:
        print("错了，大了")
    elif num < n:
        print("错了，小了")
    else:
        print("正确")
        break

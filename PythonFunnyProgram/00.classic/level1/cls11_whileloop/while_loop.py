########## 求 [1, 100] 的整数的和

n = 1
sum = 0

while n <= 100:
    sum = sum + n
    n = n + 1

print(sum)

########## 求 [100, 500] 的整数的和

n = 100
sum = 0

while n <= 500:
    sum = sum + n
    n = n + 1

print(sum)

########## 求 [1, 100] 的所有奇数的和

n = 1
sum = 0

while n <= 100:
    sum = sum + n
    n = n + 2

print(sum)


########## 求所有输入的正整数的和， 输入0代表结束

n = int(input('input a number: '))
sum = 0

while n > 0:
    sum = sum + n
    n = int(input('input a number: '))

print(sum)

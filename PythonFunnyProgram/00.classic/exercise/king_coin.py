coin = 0
day = int(input("请输入天数"))
cur = 0
total = 0

while cur + coin + 1 <= day:
    coin += 1
    total += coin * coin
    cur += coin

total += (day - cur) * (coin+1)

print(total)



#cur = 0
total = 0
coin = 1
counter = 0
for i in range(day):
    total += coin
    counter += 1
    if counter == coin:
        counter = 0
        coin += 1

print(total)

a = (0,1,4)
print(max(a))


#
day = int(input())

count = 0
total = 0
coin = 1

for d in range(day):
    sum += coin
    count += 1
    if count == coin:
        count = 0
        coin += 1

print(total)
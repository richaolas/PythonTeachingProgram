sum_val = 0

for i in range(2, 101):
    # sum = sum + i
    flag = True
    for n in range(2, i):
        if i % n == 0:
            flag = False
            break
    if flag:
        sum_val += i

print(sum_val)

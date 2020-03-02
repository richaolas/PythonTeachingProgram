import random
arr = []
for i in range(10):
    arr.append(random.randint(1, 5))
print('随机数组',arr)
arr.sort()
arr2 = []
for i in arr:
    for j in arr2:
        if arr.count(i) == int(j[2]):
            break
    else:
        if str(i) + '_' +  str(arr.count(i)) not in arr2:
            arr2.append(str(i) + '_' +  str(arr.count(i)))
print('统计结果：', arr2)

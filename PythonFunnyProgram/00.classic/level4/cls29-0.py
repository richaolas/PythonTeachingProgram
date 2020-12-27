import sys
print(sys.version)

#a = [1, 1, 1, 2, 1, 3, 4, 5, 1, 1, 1]
a = [1, 1, 1, 1, 2, 1]

cnt = 0

for i in a:
    cnt = cnt + 1
    print('No:', cnt, 'item:', i)
    print(a)
    if i == 1:
        a.remove(i) #remove the first item which equal to i
    print(a)

print(a)


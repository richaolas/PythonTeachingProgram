import random

nums = [10, 7, 6, 6, 6, 5, 5, 4, 2, 2, 1]

cnts = []

for i in range(len(nums)):
    cnts.append(nums.count(nums[i]))

print(cnts)
cnts.sort()
cnts.reverse()
print(cnts[0])

for i in range(len(nums)):
    if nums.count(nums[i]) == cnts[0]:
        print('The most frequent number is', nums[i])
        break

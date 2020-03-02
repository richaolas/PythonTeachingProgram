import random

nums = [10, 7, 6, 6, 6, 5, 5, 5, 4, 2, 2, 1]

cnts = []

for i in range(len(nums)):
    cnts.append(nums.count(nums[i]))

print(cnts)
cnts.sort()
cnts.reverse()
print(cnts[0])

for i in range(len(nums)):
    if nums.count(nums[i]) == cnts[0]:
        print(nums[i])
        #break


# nums = []
# for i in range(10):
#     nums.append(random.randint(1, 10))
#
# print(nums)
#
# ### Question ?
# nums.sort()
#
# print(nums)
#
# nums.reverse()
#
# print(nums)
#
# nums = [10, 9, 9, 8, 6, 6, 6, 4, 3, 1]
#
# print(nums.index(3))
# print(nums.count(9))
# print(nums.count(0))


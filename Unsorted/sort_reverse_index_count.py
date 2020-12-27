import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1,10))

print(numbers)

print(numbers.index(8))
print(numbers.count(1))
#print(numbers.index(0))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)





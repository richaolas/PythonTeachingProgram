import random

list = []
for i in range(50):
    list.append(random.randint(1, 100))

numbers = []
for i in range(len(list)):
    if list[i] not in numbers:
        numbers.append(list[i])

counter = []
for num in numbers:
    counter.append([num, list.count(num)])

counter.sort(key=lambda x: x[0], reverse=True)

print(counter)

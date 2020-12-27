li1 = ['Q1-1', 'Q1-2', 'Q1-3']
li2 = ['Q2-1', 'Q2-2', 'Q2-3', 'Q2-4']

print(li1 + li2)
print(li1)
print(li2)

li1.extend(li2)
print(li1)
print(li2)

li1.remove(li1[0])
del li1[len(li1) - 1]

print(li1)
print(li2[1:4:2])  # 1, 3

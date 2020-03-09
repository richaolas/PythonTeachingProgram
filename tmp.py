def j(x):
    s = []
    for i in x:
        if i % 2 == 1:
            s.append(i)
    return s

print(j([1,2,34,5,6,7,7,76,76]))

# def g(x):
#     if x>=0:
#         return x
#     else:
#         return -x
# x=-10.5
# print(g(x))
#
# def a(x):
#     s=0
#     for i in x:
#         s+=i
#     #len(x)
#     return s/len(x)
#
# print(a([1,2,3,4,5]))
# print(a({1:'3', 2:'8'}))
#
#
#
#
#
#
#
#
#
#



#
#
#
#
# import random
#
# def add(a, b):
#     c = a + b
#     return c
#
#
# def getsum(a):
#     s = 0
#     for i in a:
#         s += i
#     return s
#
#
# x = add(1, 2)
# print(x)
# y = add(24, 90)
# print(y)
#
# s = getsum([1,2,3,4,5,6])
# print(s)
#
# s = getsum((4,5,6,7,7,8))
# print(s)
#
# add(random.randint(10,100), random.randint(9,80))

#python——map和filter的使用
#python内置函数map和filter都是对一个序列进行相应的操作，map是对每一元素做自定义的映射，filter是对序列每个元素过滤。

# filter（fun，sequence）
# 参数fun可以是一个自定义的函数名，也可以使用lambda函数。参数sequence是一个序列，
# 可以是列表、元组或者字符串 。函数对序列每一元素做出条件判断，并把所有的True元素返回，返回对象是一个迭代器。如下所示：

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fun(a):
    return a % 2 == 0

res = filter(lambda x: x > 5, a)
print(res)
print(list(res))

res1 = filter(fun, a)
print(res1)
print(list(res1))

# map（fun，sequence）
# 参数上map函数与filter是一样的，他们的差别就是函数是对每个元素做一个数学上的代换，而非条件的判断。这个函数返回的也是一个迭代器。如下所示：

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [2, 3, 4, 5, 6, 7, 8, 9, 0]

def fun(a):
    return a + 1

res = map(lambda x, y: x + y, a, b)
print(res)
print(list(res))

res1 = map(fun, a)
print(res1)
print(list(res1))

# reduce（fun，sequence）
# 参数是与上面两个是一样的，他的功能是对一个序列进行压缩运算，得到一个值。但是reduce在python2的时候是内置函数，到了python3移到了functools模块，所以使用之前需要
# from functools import reduce 。与上面的区别是，该函数返回一个值，而非迭代器，且fun函数必须传入两个参数。如下所示：
#
# from functools import reduce
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def fun(a, b):
#     return a * b
#
#
# res = reduce(lambda x, y: x + y, a)
# print(res)
# res1 = reduce(fun, a)
# print(res1)
# 45
# 362880
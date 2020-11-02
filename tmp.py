wordBook = {'red':'红色', 'desk':'桌子', 'food':'食物', 'car':'车子', 'gun':'枪'}
#接下来就是开始我们每一轮的检查啦，直到不需要检查为止
checkBook = wordBook.copy()

print(id(wordBook['red']))
del wordBook['red']
print(id(checkBook['red']))

print("床前明月光")
print("依珊以上雙")
print("舉頭望明月")
print("低頭思故鄉")


import turtle
turtle.pensize(30)
turtle.dot()
turtle.pensize(1)
turtle.forward(60)
turtle.pensize(30)
turtle.dot()
#turtle.forward(-100)
turtle.done()



# # s = ([4],[3],[2],[1])
# # s = (list((1,2,3,4)))
# # s = tuple([1,2,3,4])
# #
# # s = str([1,2,3,4,5])
# # s = tuple('string')
# # print(s)
# # #有一个元组 a = (1,2,3,4,5)
# # #利用将元组a 得到一个新元组 b = (2,4,6,8,10)
# # #要求：便利元组每一个元素，然后x2，放到一个列表中，再将这个列表转换为元组输出
# # #print(list(1))
# #
# # print(tuple([[1,2,3]]))
#
# t = (1,2,3)
# #s = t[0:1] + 3 + t[2:]
# #print(s)
#
# print(max(1,2))
# print(max([12,9,3,4,4,]))
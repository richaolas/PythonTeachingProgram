# -*- coding: UTF-8 -*-

dict = {'red': '红色', 'desk':'桌子', 'food':'食物', 'car':'车子', 'gun':'枪'}
#然后用for循环逐一去判断
for i in dict.keys():
    print(i + "是什么意思？")
    yourAnswer = input("回答:")
    if yourAnswer == dict[i]:
        print("回答正确")
    else:
        print("回答错误")

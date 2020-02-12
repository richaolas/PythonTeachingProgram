#练习
import random

'''
#1. 1+2+3...+100
'''
sum = 0
for i in range(1,100):
    sum+=i
print(sum)

'''
#2. 35选7
'''
vallist = []
for i in range(1,36):
    vallist.append(i)
print(vallist)

vallist = [i for i in range(1,36)]
print(vallist)

sellist = []
for i in range(0,7):
    randomIdx = random.randint(0,len(vallist)-i-1)
    sellist.append(vallist[randomIdx])
    del vallist[randomIdx]
print(sellist)
print(vallist)

#3
import tkinter                                  #导入 tkinter 模块
root = tkinter.Tk()                             #创建主窗口
w = tkinter.Label(root, text='你好,Python!')    #创建标签类的实例对象
w.pack()                                        #打包标签
root.mainloop()                                 #开始事件循环
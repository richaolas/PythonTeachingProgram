#创建我们的生词本
wordBook = {'教师':'tutor', '向前':'forward', '后退':'backward', '右转':'right', '左转':'left', '海龟':'turtle'}
#需要一个变量来帮我们识别用户是否需要巩固，第一次当然默认是需要巩固的
needCheck = True
#创建待检测单词本，最开始需要检查所有单词，我们需要copy，因为不希望改变原有生词本
checkBook = wordBook.copy()
#接下来就是开始我们每一轮的检查啦，直到不需要检查为止
while needCheck:
    #因为不能在for循环的时候删除元素，先copy一个临时字典作为循环使用
    tmp = checkBook.copy()
    #然后对检查本里的单词逐个检查
    for i in tmp:
        print(i + '如何拼写')
        yourAnswer = input('回答:')
        #如果回答正确就把这个单词从检测单词本中删掉，代表用户已经掌握了
        if yourAnswer == tmp[i]:
            print('回答正确')
            del checkBook[i]
        else:
            print('回答错误')

    if checkBook: # 如果还有没有掌握的单词
        print(' '.join(checkBook.keys()))
        key = input('要不要再复习一遍错误的单词(Y/N)')
        if key == 'N':
            needCheck = False
    else:
        print('恭喜你掌握了全部单词！')
        needCheck = False

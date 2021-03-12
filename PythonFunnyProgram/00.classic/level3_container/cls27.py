#创建我们的生词本
wordBook = {'教师':'tutor', '向前':'forward', '后退':'backward', '右转':'right', '左转':'left', '海龟':'turtle'}
#需要一个变量来帮我们识别用户是否需要巩固，第一次当然默认是需要巩固的
needCheck = True
#接下来就是开始我们每一轮的检查啦，直到不需要检查为止
checkBook = wordBook
while needCheck:
    #首先把需要检查的单词都放到检查本里
    #checkBook = wordBook.copy()
    wrongWord = {}
    #然后对检查本里的单词逐个检查
    for i in checkBook.keys():
        print(i + '如何拼写')
        yourAnswer = input('回答:')
        #如果回答正确就把这个单词从生词本中删掉，代表用户已经掌握了
        if yourAnswer == checkBook[i]:
            print('回答正确')
        else:
            wrongWord[i] = checkBook[i]
            print('回答错误')

    if wrongWord:
        print(' '.join(wrongWord.values()))
        key = input('要不要再复习一遍错误的单词(Y/N)')
        if key == 'N':
            needCheck = False
        else:
            checkBook = wrongWord
            needCheck = True
    else:
        print('恭喜你掌握了全部单词！')
        needCheck = False

test = {'教师':'tutor', '向前':'forward'}
# 后退:backward
# 右转:right
# 左转:left
# 海龟:turtle

#首先我们需要一个变量来帮我们识别用户是否需要巩固，第一次当然默认是需要巩固的
needCheck = 'y'
#然后创建我们的生词本
wordBook = {'red':'红色', 'desk':'桌子', 'food':'食物', 'car':'车子', 'gun':'枪'}
#接下来就是开始我们每一轮的检查啦，直到不需要检查为止
while needCheck == 'y':
#首先把需要检查的单词都放到检查本里
    checkBook = wordBook.copy()
#然后对检查本里的单词逐个检查
    for i in checkBook.keys():
        print(i + '是什么意思')
        yourAnswer = input('回答:')
#如果回答正确就把这个单词从生词本中删掉，代表用户已经掌握了
        if yourAnswer == checkBook[i]:
            del wordBook[i]
            print('回答正确')
        else:
            print('回答错误')


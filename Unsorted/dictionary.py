wordBook = {'tall': ['高','长','夸大的'],
     'short':['短', '矮'],
     'fat':  ['胖'],
     'thin': ['瘦']}

needcheck = 'y'

while needcheck == 'y':
    checkbook = wordBook.copy()
    for key in checkbook:
        print('tell me mean of the word: ' + key)
        answer = input('input your answer: ')
        if answer in checkbook[key]:
            print('you are right')
            del wordBook[key]
        else:
            print('sorry, your answer is wrong!')
    if len(wordBook.keys()) != 0:
        needcheck = input(' '.join(wordBook.keys()) + '这些单词还需要巩固一下需要吗?(y/n)')
    else:
        needcheck = 'n'
        print('恭喜你，全部答对了!')

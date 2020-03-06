wordBook = {'tall': ['高','长','夸大的'],
     'short':['短', '矮'],
     'fat':  ['胖'],
     'thin': ['瘦']}

checkbook = wordBook.copy()
print(len(checkbook))

while len(checkbook) > 0:
    for key in checkbook:
        print('tell me mean of the word: ' + key)
        answer = input('input your answer: ')
        if answer in checkbook[key]:
            print('you are right')
            del wordBook[key]
        else:
            print('sorry, your answer is wrong!')
    checkbook = wordBook.copy()


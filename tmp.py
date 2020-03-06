# d={'gao':'tall','ai':'short'}
# d['pang']='fat'
# d['shou']='thin'
# print(d)
#
# for key in d:
#     print('chinese:' + key , 'English:' + d[key])

#1+2+...+20

n = 1
sum = 0
while n <= 20:
    sum = sum + n
    n = n + 1

print(sum)


# d = {'tall': ['高','长','夸大的'],
#      'short':['矮'],
#      'fat':  ['胖'],
#      'thin': ['瘦']}

#print(d)
#del d['tall']

# n = 10
# while n > 0:
#     print(n)
#     n = n - 1



#print(d)


#counter = 0

while len(d) > 0:
    for key in d:
        print('tell me mean of the word: ' + key)
        chinese = input('input your answer: ')
        if chinese in d[key]:
            print('you are right')
            del d[key]
            #counter = counter + 1
        else:
            print('sorry, your answer is wrong!')

#print(counter)

li = [ ] #空列表
for i in range(5):
    question = input('input your question: ')
    li.append(question)

for i in range(len(li)): # 0,1,2....N-1
    print(i, li[i])
print(li)

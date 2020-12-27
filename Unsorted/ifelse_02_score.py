score = int(input('Please input your score: '))

if score >= 90:
    print('A')
#if score >= 80 and score < 90:
if 80 <= score < 90:
    print('B')
#if score >= 60 and score < 80:
if 60 <= score < 80:
    print('C')
if score < 60:
    print('D')
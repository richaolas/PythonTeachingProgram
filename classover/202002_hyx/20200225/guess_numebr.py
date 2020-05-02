import random

target = random.randint(0,10)
print(target)

guessed = False

for i in range(3):
    num = int(input('Please input number which you guess: '))
    if num == target:
        print('you are right')
        guessed = True
        break
    elif num < target:
        print('your number is less')
    else:
        print('your number is greater')

if guessed: # if guessed == True
    print("congratulation")
else:
    print('sorry you loss.')
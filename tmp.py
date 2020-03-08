import random

li = [1,2,3]

for i in li:
    print(i)


wordCount = 10

while wordCount < 100:
    #wordCount += random.randint(0, 10)
    num = random.randint(0, 10)
    wordCount = wordCount + num

print('finally I learn %d' % (wordCount))


isQuitButtonPressed = False

while not isQuitButtonPressed:
    print('play the game')
    answer = input('Do you want play(y/n)?')
    if answer == 'n':
        isQuitButtonPressed = True


random.randint(0, 10)

def add(a, b):
    c = a + b
    return c

result = add(100, 200)
print(result)


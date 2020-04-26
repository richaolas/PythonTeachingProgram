music = open('data/music.txt')
lines = music.readlines()
line1 = lines[0]
line2 = lines[1]
print(line1)
nums = line1.split(' ')
print(nums)
keys = []
for n in nums:
    a = n.strip(' \n')
    keys.append(int(a))

print(keys)

vals = []
for n in line2.split(' '):
    vals.append(n.strip(' \n'))

keyVal = {}
for (idx, k) in enumerate(keys):
    keyVal[k] = vals[idx]

print(keyVal)

music.close()

star = open('data/star.txt')
result = open('data/result', 'w')
for c in star.read():
    print(c)
    if c in ('1','2','3','4','5','6','7'):
        result.write(keyVal[int(c)]+' ')

result.close()
star.close()



import turtle

turtle.speed(0)
turtle.bgcolor('skyblue')
w = turtle.window_width()
h = turtle.window_height()

turtle.fillcolor('blue')
turtle.pencolor('blue')
turtle.begin_fill()

turtle.goto(-w/2, 0)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(h/2)

turtle.end_fill()

turtle.begin_fill()
turtle.goto(-200, -10)
turtle.goto(0, 100)
turtle.setheading(180+20)
turtle.circle(100, 180)
turtle.goto(-200, -10)
turtle.end_fill()

turtle.begin_fill()
turtle.goto(200, -10)
turtle.goto(300, 50)
turtle.setheading(180+20)
turtle.circle(100, 180)
turtle.goto(200, -10)
turtle.end_fill()

# turtle.begin_fill()
# turtle.goto(-200, -250)
# turtle.circle(400)
# turtle.end_fill()
# turtle.begin_fill()
# turtle.goto(300, -350)
# turtle.circle(400)
# turtle.end_fill()

turtle.done()




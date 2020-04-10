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




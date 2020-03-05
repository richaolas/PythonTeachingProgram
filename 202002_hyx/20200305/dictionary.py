d = {}
print(type(d))
d['男孩'] = 'boy'  # (key, value) ('男孩'，boy) d[key] = value
d['女孩'] = 'girl'
d['老师'] = 'teacher'
print(len(d))

print(d['老师']) #dict[key]

s = {}
s['age'] = 18
s['name'] = '张三'
s['id'] = 2020001

print(s)

li = []
li = [1,2,3,4]

s = {'age':18, 'name':'张三', 'id':2020001}
print(s)


li = [1,2,3,4,5]
for item in li:
    print(item)

for item in d:
    print(item, d[item])



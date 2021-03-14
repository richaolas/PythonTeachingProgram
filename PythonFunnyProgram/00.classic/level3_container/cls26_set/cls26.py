stu1 = {'name':'sihan', 'age':13, 'hobby':{'art','game','program'}}
stu2 = {'name':'ric', 'age':15, 'hobby':{'sport','game','program'}}
stu3 = {'name':'hong', 'age':14, 'hobby':{'music','sing','dance'}}

students = [stu1, stu2, stu3]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        si = students[i]
        sj = students[j]
        #if len ( si['hobby'] & sj['hobby'] ) > 0:
        if si['hobby'] & sj['hobby']:
            print(si['name'] + ' and ' + sj['name'] + ' will be friends.')

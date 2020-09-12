q = [10, 20, 93,81,85,92,0,1,2,100]
#w = q
#w.sort()
#print(w)


for e in range(len(q)):
    a = e
    for s in range(a+1,len(q)):
        if s < a:
            a = s
    q[a], q[e] = q[e], q[a]
print(q)

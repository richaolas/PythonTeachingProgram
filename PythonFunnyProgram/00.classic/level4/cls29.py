#是否是数字
def isnum(c):
    return c not in '+-*/'

#分离数字和操作符
def splitCal(content):
    numLst = []
    opLst = []
    start = -1
    for i in range(len(content)):
        if isnum(content[i]) and start < 0:
            start = i
        if not isnum(content[i]):
            opLst.append(content[i])
            numLst.append(float(content[start:i]))
            start = -1
    numLst.append(float(content[start:]))

    return numLst, opLst


def calc2(numLst, opLst):
    numtmp = []
    optmp = []

    numtmp.append(numLst.pop(0))
    for op in opLst:
        if op in '/*':
            numtmp[-1] = cal(numtmp[-1], op, numLst.pop(0))
        else:
            if len(optmp) > 0:
                numtmp[-1] = cal(numtmp.pop(-2), optmp.pop(-1), numtmp[-1])

            optmp.append(op)
            numtmp.append(numLst.pop(0))

    return cal(numtmp[0], optmp[0], numtmp[1])

def calc(numLst, opLst, callist):
    i = 0
    while i < len(opLst):
        if opLst[i] in callist:
            numLst[i] = cal(numLst[i], opLst[i], numLst[i+1])
            del opLst[i]
            del numLst[i+1]
        else:
            i += 1

def calculator(numLst, opLst):
    calc(numLst, opLst, '*/')
    calc(numLst, opLst, '+-')
    return numLst[0]


#计算两个数的四则运算
def cal(a,op,b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b

#s = cal(2, "/", 2)

s = '1*8+90-100/3+8*7-6*6*6/5'
#s = '1+8*9+9-100'
#s = '1*1'
numLst, opLst = splitCal(s)
print(numLst, opLst)
#print(calc(numLst, opLst), eval(s))
print(eval(s))
assert (eval(s) == calculator(numLst, opLst))
print(calculator(numLst, opLst))
#li = [1,2,3]

#for i in li:
#    print(i)
#    li.remove(li[0])


#for op in opLst:
# for i in range(len(opLst)):
#     if opLst[i] in '*/':
#         numLst.remove()

#for op in opLst:
# li = []
#
# print(li.pop())
# print(li)

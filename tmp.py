#是否是数字
def isnum(c):
    if c not in '+-*/':
        return True
    return False

#分离数字和操作符
def splitCal(content):
    numLst = []
    opLst = []
    temp = ''
    for i in range(len(content)):
        if isnum(content[i]):
            if i == len(content) - 1:
                numLst.append(float(content[len(temp) + 1:]))
        else:
            if content[i] != '.':
                start = len(temp)
            else:
                1/0
            if start > 0:
                start = len(temp) + 1
            numLst.append(float(content[start:i]))
            opLst.append(content[i])
            temp = content[:i]
    return numLst, opLst


a, b = splitCal("  300.01   +4  *5+6-7")
print(a, b)
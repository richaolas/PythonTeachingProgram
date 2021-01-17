t1 = int(input('Add the bigger number here: '))
t2 = int(input('Add the smaller number here: '))

t1 = int(t1)
t2 = int(t2)

r1 = t1 + t2
r2 = t1 - t2
r3 = t1 * t2
r4 = t1 / t2
# // 地板除，商舍去小数部分
# % 求余数
r5 = t1 % t2

print("Sum = " + str(r1) + ", Difference = " + str(r2) + ", Product = " + str(r3) + ", Quotient = " + str(r4) + ''', and 
Remainder = ''' + str(r5))

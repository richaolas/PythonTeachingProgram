a = [[2, 3, 4], [5, 6, 7]]  # 2x3
b = [[1, 2], [3, 4], [5, 6]]  # 3x2

#
# 2 3 4   1 2   31 40
# 5 6 7   3 4
#         5 6
#
c = []
for i in range(len(a)):
    row = []
    for j in range(len(b[0])):
        val = 0
        for k in range(len(a[0])):
            val += a[i][k] * b[k][j]
        row.append(val)
    c.append(row)

print(c)

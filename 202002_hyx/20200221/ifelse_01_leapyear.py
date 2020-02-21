year = int(input('Please input year: '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('闰年')
else:
    print('平年')

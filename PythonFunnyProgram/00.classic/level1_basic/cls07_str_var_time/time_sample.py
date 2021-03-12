import time

print(time.time())  #获得系统此刻的时间戳
print(time.strftime("%H:%M:%S")) ##24小时格式
print(time.strftime("%I:%M:%S"))## 12小时格式
print(time.strftime("%Y/%m/%d  %I:%M:%S"))## 带日期的12小时格式
import time
name = input('input your name: ')
t = input('input sleep time: ')
time.sleep(int(t))
print(('Wake Up ' + name)*3)
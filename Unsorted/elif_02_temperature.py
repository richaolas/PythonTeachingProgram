temperature = int(input('please input temperature: '))

if temperature < -1:
    print('too cold')
elif 10 < temperature < 30:
    print('normal')
elif temperature > 35:
    print('too hot')
else:
    print('I don not care')
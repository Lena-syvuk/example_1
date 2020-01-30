a = 7
b = 10
c = 1
while (a + c)<=b:
    print (a + c, 'пока что нет')
    a +=1
    if (a + c) > b:
        print('дождались')
        print(a)

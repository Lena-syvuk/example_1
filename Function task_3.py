import random
def list(lenght, max):
    result = []
    l1 = []
    l2 = []
    for x in range(0,lenght):
        l1.append(random.randint(-10, max))
        l2.append(random.randint(-10, max))
    for x in l1:
        for y in l2:
            if x == y:
                result.append(x)
    return result






print('Введите lenght:')
lenght = int(input())
print('Введите max:')
max = int(input())
asd = list(lenght,max)
print(asd)


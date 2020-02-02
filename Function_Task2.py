import random
def list(lenght, max):
    result = []
    for x in range(0,lenght):
        result.append(random.randint(-10, max))
    return result

def list2(arg):
    result = []
    for x in arg:
        if x > 7:
            result.append(x)
    return result

print('Введите lenght:')
lenght = int(input())
print('Введите max:')
max = int(input())
asd = list(lenght,max)

a = list2(asd)
print(asd)
print (a)
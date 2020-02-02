import random
def list(lenght, max):
    result = []
    for x in range(0,lenght):
        result.append(random.randint(-10, max))
    return result

print('Введите lenght:')
lenght = int(input())
print('Введите max:')
max = int(input())

asd = list(lenght,max)
print (asd)








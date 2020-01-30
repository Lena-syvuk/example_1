print('Введите A:')
a = int(input())
print('Введите B:')
b = int(input())
print('Введите C')
c = int(input())
z = int(a) + int(c)
q = int(b) - int(c)
if a > b:
    print('Совершилось')
elif b > a:
    print(' Да ну')
elif a == b:
    print('А если так')
elif z > c:
    print('Совершилось')
elif z < c:
    print('Да ну')
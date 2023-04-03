while True:
    a1 = input('Введите число А1: ')
    d = input('Вdедите число D: ')
    n = input('Вdедите число N: ')
    if a1.isdigit() == False:
        print('Неверный тип A1')
    elif d.isdigit() == False:
        print('Неверный тип D')
    elif n.isdigit() == False:
        print('Неверный тип N')
    else:
        break
a1 = int(a1)
d = int(d)
n = int(n)

for i in range(n):
    print(a1 + i * d)

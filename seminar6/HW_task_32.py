import random

array1 = [random.randint(-10, 8) for i in range(10)]
print(array1)

while True:
    a = input('Введите число  ')
    b = input('Вdедите число ')
    if a.isdigit() == False:
        print('Неверный тип A')
    elif b.isdigit() == False:
        print('Неверный тип B')
    else:
        break


min_number = int(a)
max_number = int(b)

for i in range(len(array1)):
    if min_number <= array1[i] <= max_number:
        print(i)

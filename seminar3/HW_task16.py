# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2
import random

while True:
    n = input('Введите число N - длина массива: ')
    x = input('Введите Число которое необходимо проверить X: ') 
    if n.isdigit() == False:        
        print('Неверный тип N') 
    elif x.isdigit() == False:
        print('Неверный тип X') 
    else: 
        break

n = int(n)
x = int(x)
b = int(n/2)

array = [random.randint(1, b) for i in range(n)]
print(array)
count = 0
for i in range(len(array)):
    if array[i] == x: 
        count =+ 1
print(f'Вывод:  {count}')
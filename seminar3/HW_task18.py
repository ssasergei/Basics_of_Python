# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

while True:
    N = input('Введите число N - длина массива: ')
    if N.isdigit() == False:
        print('Неверный тип N')
    else:
        break
N = int(N)
# b = int(n/2)
array = [random.randint(1, N) for _ in range(N)]
print(array)

while True:
    X = input('Введите Число которое необходимо проверить X: ')
    if X.isdigit() == False:
        print('Неверный тип X: ')
    else:
        break
X = int(X)

result = array[0]

set_array = set(array)
# print (set_array)
for i in set_array:
    if i/X <= 1:
        result = i

print(f' Самое близкое число к {X} -> {result}')

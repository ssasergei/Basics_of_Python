'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''
import random
# проверка ввода
while True:
    N = input('кол-во элементов первого множества N: ')
    M = input('кол-во элементов второго множества M: ')
    if N.isdigit() == False:
        print('Неверный тип N')
    elif M.isdigit() == False:
        print('Неверный тип M')
    else:
        break

N = int(N)
M = int(M)

array1 = [random.randint(1, 15) for i in range(N)]
array2 = [random.randint(1, 15) for i in range(M)]

# преобразование массива в множество
array1 = set(array1) 
array2 = set(array2)
result = array1.intersection(array2)

print(*sorted (array1))
print(*sorted(array2))
if (len(result) == 0):
    print('нет совпадений')
else:
    print(*sorted (result))
'''
Задача 33:
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
import random

def ReplaceNum(arr, min, max):
    for i in arr:
        if i==max: arr[arr.index(i)] = min
    return arr

N = int(input('введите количество элементов массива N: '))
array = [random.randint(1, 5) for _ in range(N)]
print(array)
print(ReplaceNum(array, min(array), max(array)))
'''
Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
'''

while True:
    a = input('кол-во элементов первого множества a: ')
    b = input('кол-во элементов второго множества b: ')
    if a.isdigit() == False:
        print('Неверный тип a')
    elif b.isdigit() == False:
        print('Неверный тип b')
    else:
        break
a = int(a)
b = int(b)

def SumNumber (start,end):
    if start==0:
        return end
    return SumNumber(start - 1, end + 1 )

print(SumNumber(a,b)) 

    


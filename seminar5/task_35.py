'''
задача 35:
Напишите функцию, которая принимает одно число и 
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое 
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''
def ReturnPriznak(n):
    priznak = 1
    for i in range(2, n-1):
        if n%i == 0: priznak = 0
    return priznak

Num = int(input('Введите простое число '))
print(bool(ReturnPriznak(Num)))
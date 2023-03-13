# Задача №2
# Найти сумму цифр трехзначного числа.
# 123 -> 6 (1+2+3)
# 100 -> 1 (1+0+0)

while True: 
    i = (input ('Введите число: '))
    print(i.isdigit())
    if i.isdigit() == False:
        print('Неверный тип') 
    else: 
        break

a = int(i) / 100
b = (int(i) % 100) / 10 
c = int(i) % 10
sum = int(a) + int(b) + int(c)
print(i, '->', sum, '(', int(a), '+', int(b), '+', int(c), ')')
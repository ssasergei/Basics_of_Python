# Задача №6
# Вы пользуетесь общественным транспортом? Вереятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма
# первых трех  цифр равна сумме последних Т.е. билет с номером 385916 - счастливый.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

while True: 
    i = input ('Введите 6 значный билета билета: ')
    if i.isdigit() == False:
        print('Неверный тип номера')
     
    else: 
        break

sum1  = int(i[0]) + int(i[1]) + int(i[2])
sum2  = int(i[3]) + int(i[4]) + int(i[5])
yes = sum1==sum2

if yes == False:
    print(i,'-> no')
else:
    print(i,'-> yes')    

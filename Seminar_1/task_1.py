#Напишите программу, 
#которая принимает на вход 2 числа и проверяет, 
#является ли одно число квадратом другого.

#Примеры:

#5, 25 -> да
#4, 16 -> да
#25, 5 -> да
#8, 9 -> нет

print('Здравствуте! Напишите первое число: ')
numberOne = int(input())

print('Напишите второе число: ')
numberTwo = int(input())

if numberOne*numberOne==numberTwo:
    print(f'{numberOne} является квадратом числа {numberTwo}!')
elif numberTwo*numberTwo==numberOne:
    print(f'{numberTwo} является квадратом числа {numberOne}!')
else:
    print('Ни одно из чисел не является квадратом другого!')
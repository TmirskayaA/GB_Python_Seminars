#Напишите программу, 
#которая принимает на вход число N 
#и выдаёт последовательность из N членов.

#*Пример:*

#Для N = 5: 1, -3, 9, -27, 81

print('Здравствуте!')
number = int(input('Напишите число: '))

import random

listNumber = []

for i in range(0, number):
    listNumber.insert(i, int(random.randrange(-99,99)))

print(f'Последовательность из {number} чисел: {listNumber}')

#Реализуйте алгоритм задания случайных чисел 
#без использования встроенного генератора псевдослучайных чисел.

print('Здравствуте!')
max = int(input('Задайте максимум: '))

import datetime 

number = datetime.datetime.now().microsecond%max
print(number)
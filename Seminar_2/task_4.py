#Создайте список из случайных чисел. 
#Найдите максимальное количество 
#его одинаковых элементов.

print('Здравствуте!')
number = int(input('Сколько чисел будет в списке? '))

import random

listNumber = []

for i in range(0, number):
    listNumber.insert(i, int(random.randrange(1,9)))

print(f'Новый список: {listNumber}')

count = 0
massive = []

for i in range(len(listNumber)):
    if listNumber.count(listNumber[i]) > 1: 
        count += 1
        if listNumber[i] not in massive: massive.append(listNumber[i])

print(f'Повторяющиеся элементы = {massive}.')
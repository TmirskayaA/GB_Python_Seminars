#Задайте список. 
#Напишите программу, которая определит, 
#присутствует ли в заданном списке строк некое число.

print('Здравствуте!')
counter = int(input('Сколько элементов будет в вашем списке? '))
typeData = str(input('Какого типа будут данные в вашем списке? '))

def DefiningDataType(type):
    if type == 'числовой': return int
    elif type == 'текстовый': return str
    elif type == 'вещественный': return float
    elif type == 'список': return list
    elif type == 'логический': return bool
    else: return 'error'

def FillArray(quantity, type):
    array = []
    for i in range(0, quantity):
        element = type(input(f'Задайте {i+1} элемент: '))
        array.append(element)
    return array

def HaveDigit(array):
    for i in range(0, len(array)):
        if array[i].isdigit(): return True

if DefiningDataType(typeData) == 'error': 
    print('Не смогли определить тип данных.')
    exit()

newArray = FillArray(counter, DefiningDataType(typeData))

print(f'Ваш список: {newArray}')

if HaveDigit(newArray): print('В этом списке есть число!')
else: print('В этом списке числа нет.')
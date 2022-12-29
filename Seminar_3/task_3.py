#Напишите программу, 
#которая определит позицию 
#второго вхождения строки в списке 
#либо сообщит, что её нет.

#Пример:

#список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1

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

if DefiningDataType(typeData) == 'error': 
    print('Не смогли определить тип данных.')
    exit()

newArray = FillArray(counter, DefiningDataType(typeData))

print(f'Ваш список: {newArray}')

findElement = DefiningDataType(typeData)(input('Какой элемент будем искать? '))

def FirstRepeatIndex(array, element):
    replay = 0
    index = -1
    for i in range(0, len(array)):
        if array[i] == element:
            replay += 1
            if replay == 2:
                index = i
    return index

if FirstRepeatIndex(newArray, findElement) == -1: print('Такой элемент не повторяется.')
else: print(f'Этот элемент повторяется на {FirstRepeatIndex(newArray, findElement)+1} позиции!')
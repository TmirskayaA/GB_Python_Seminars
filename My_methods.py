#Определяем тип данных по его названию.
def DefiningDataType(type):
    if type == 'числовой': return int
    elif type == 'текстовый': return str
    elif type == 'вещественный': return float
    elif type == 'список': return list
    elif type == 'логический': return bool
    else: return 'error'

#Поочерёдно заполняем массив.
def FillArray(quantity, type):
    array = []
    for i in range(0, quantity):
        element = type(input(f'Задайте {i+1} элемент: '))
        array.append(element)
    return array

#Проверяет содержит ли массив числа.
def HaveDigit(array):
    for i in range(0, len(array)):
        if array[i].isdigit(): return True

#Находим индекс первого повторения объекта в массиве.
def FirstRepeatIndex(array, element):
    replay = 0
    index = -1
    for i in range(0, len(array)):
        if array[i] == element:
            replay += 1
            if replay == 2:
                index = i
    return index

#Собираем из строки числовой массив.
def CollectINTArray(string):
    array = [int(string[i]) for i in range(0, len(string)) if string[i].isdigit()]
    return array

#Метод поиска недостающего числа из Seminar_5,T1.
def WhichNumberLost(array):
    for i in range(len(array)):
        if array[i+1] - array[i] > 1:
            return array[i] + 1

#Перебираем массив и складываем из его значений новый с числами по возрастанию.
def AscendingArray(array):
    endarray = []
    max = array[0]
    endarray.append(array[0])
    for i in range(1, len(array)):
        if array[i]>max:
            endarray.append(array[i])
            max = array[i]
    return endarray

#Переводим массив в строку.
def FromArrayToString(array):
    string = array[0]
    for i in range(1, len(array)):
        string = string + " " + array[i]
    return string

#Удаляем из текста слова содержащие нежелательный объект.
def DeleteObjectInString(string, object):
    array = string.split()
    endarray = []
    endarray = [array[i] for i in range(0, len(array)) if object not in array[i]]
    
    string = FromArrayToString(endarray)
    return string

#Составляем массив из повторяющихся значений в двух других массивах.
def SearchForDoppelgangers(firstArray, secondArray):
    if len(firstArray) > len(secondArray):
        big = firstArray
        smole = secondArray
    else: 
        big = secondArray
        smole = firstArray
    
    finalArray = []

    for i in range(0, len(big)):
        if big[i] in smole: 
            if big[i] not in finalArray: finalArray.append(big[i])
    
    return finalArray
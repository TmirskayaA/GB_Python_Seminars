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

def FirstRepeatIndex(array, element):
    replay = 0
    index = -1
    for i in range(0, len(array)):
        if array[i] == element:
            replay += 1
            if replay == 2:
                index = i
    return index
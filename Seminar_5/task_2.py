#Дан список чисел. 
#Создайте список, 
#в который попадают числа, 
#описываемые возрастающую последовательность. 
#Порядок элементов менять нельзя. Пример:

#[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def AscendingArray(array):
    endarray = []
    max = array[0]
    endarray.append(array[0])
    for i in range(1, len(array)):
        if array[i]>max:
            endarray.append(array[i])
            max = array[i]
    return endarray

print('Здравствуйте!')
string = input('Нашитите числа по порядку: ')
numberMass = [int(string[i]) for i in range(0,len(string))]

print(numberMass)
print(AscendingArray(numberMass))


#В файле находится N натуральных чисел, 
#записанных через пробел. 
#Среди чисел не хватает одного, 
#чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def CollectINTArray(string):
    array = [int(string[i]) for i in range(0, len(string)) if string[i].isdigit()]
    return array

def WhichNumberLost(array):
    for i in range(len(array)):
        if array[i+1] - array[i] > 1:
            return array[i] + 1

print('Здравствуйте!')
myString = str(input('Нашитите числа по порядку: '))

#Положили числа в файл
file = open('file.txt', 'a')
file.write(" ".join(map(str, myString)))
file.close

#Считали числа из файла и собрали int массив
file = open('file.txt', 'r')
numbers = CollectINTArray(file.readline())
file.close()

print(numbers)

print(WhichNumberLost(numbers))
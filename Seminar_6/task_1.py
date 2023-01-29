#Напишите программу на Python 
#для поиска пересечения двух заданных массивов 
#с помощью Lambda.

print('Здравствуйте!\n')

string = input('Нашитите элементы для первого массива по порядку: \n')
arrayOne = [string[i] for i in range(0,len(string))]
string = input('Нашитите элементы для второго массива по порядку: \n')
arrayTwo = [string[i] for i in range(0,len(string))]

print(f'\nПервый массив: {arrayOne}\nВторой массив: {arrayTwo}')

finalArray = list(filter(lambda x: x in arrayOne, arrayTwo))

print(f'В этих двух массивах совпадают следующие элементы: {finalArray}')
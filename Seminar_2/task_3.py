#Напишите программу, 
#в которой пользователь 
#будет задавать две строки, 
#а программа - 
#определять количество вхождений 
#одной строки в другой.

print('Здравствуте!')

stringOne = str(input('Напишите то, что будет в первой строке: '))
stringTwo = str(input('Напишите то, что будет во второй строке: '))

listOne = stringOne.split()
listTwo = stringTwo.split()

print(listOne)
print(listTwo)

count = 0

for i in range(len(listOne)):
    if listOne[i] in listTwo: count += 1

print(f'Количество вхождений = {count}.')
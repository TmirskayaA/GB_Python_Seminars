#Напишите программу, 
#которая на вход принимает 5 чисел 
#и находит максимальное из них.

#Примеры:

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

print('Здравствуйте!')

listNumber = []

for i in range(5):
    print(f'Напишите {i+1} число')
    listNumber.insert(i, int(input()))

print('Ваши числа: ')
print(listNumber)

max = listNumber[0]

for i in range(5):
    if max<listNumber[i]:
        max = listNumber[i]

print(f'Максимальное число в массиве = {max}')
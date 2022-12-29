#Напишите программу, 
#которая будет на вход принимать число N 
#и выводить числа от -N до N

#*Примеры:*

#- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

print('Здравствуте! Напишите число: ')
number = int(input())

listNumber = []
minoreNumber = number*-1

for i in range(0, number*2+1):
    listNumber.insert(i, int(minoreNumber+i))

print(f'{number} -> {listNumber}')
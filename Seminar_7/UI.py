def GetData():
    print('\nЗдравствуйте!\n')
    print('->|Сложение|Вычитание|Умножение|Деление|Получение остатка|Возведение в степень|<-\n')
    
    choise = str(input('Какую операцию хотите выполнить? '))
    x,y,operation = ActionComponents(choise)
    if x == 'error': 
        print('\nНе смог распознать операцию. Напишите её в точности как показано выше.')
        exit()
    else:
        digitX = int(input(f'\nЗадайте {x}: '))
        digitY = int(input(f'Задайте {y}: '))
        return digitX, digitY, operation

def ActionComponents(operation):
    if operation == 'Сложение':
        patternx = 'первое слогаемое'
        patterny = 'второе слогаемое'
        typeOperation = 'сложения'
    elif operation == 'Вычитание':
        patternx = 'уменьшаемое'
        patterny = 'вычитаемое'
        typeOperation = 'вычитания'
    elif operation == 'Умножение':
        patternx = 'первый множитель'
        patterny = 'второй множитель'
        typeOperation = 'умножения'
    elif operation == 'Деление':
        patternx = 'делимое'
        patterny = 'делитель'
        typeOperation = 'деления'
    elif operation == 'Получение остатка':
        patternx = 'делимое'
        patterny = 'делитель'
        typeOperation = 'получения остатка'
    elif operation == 'Возведение в степень':
        patternx = 'основание степени'
        patterny = 'показатель степени'
        typeOperation = 'возведения в степень'
    else:
        patternx,patterny,typeOperation = 'error'

    return patternx, patterny, typeOperation

def PrintResult(type, result):
    print(f'\nРезультат {type} = {result}')
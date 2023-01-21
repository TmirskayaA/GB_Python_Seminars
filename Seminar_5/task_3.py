#Напишите программу, 
#удаляющую из текста все слова, 
#содержащие "абв".

def FromArrayToString(array):
    string = array[0]
    for i in range(1, len(array)):
        string = string + " " + array[i]
    return string

def DeleteObjectInString(string, object):
    array = string.split()
    endarray = []
    endarray = [array[i] for i in range(0, len(array)) if object not in array[i]]
    
    string = FromArrayToString(endarray)
    return string

print('Здравствуйте!')
text = input('Напишите фразу: ')

objectToDelete = input('Что не должно содержаться в словах? ')

print(f'Удалили все слова, содержащие {objectToDelete}: {DeleteObjectInString(text, objectToDelete)}')
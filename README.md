# Seminar 1

Tasks:

1. Напишите программу, которая принимает на вход 2 числа и проверяет, является ли одно число квадратом другого.
Примеры:

- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8, 9 -> нет

2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. Примеры:

- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90

3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N. Примеры:

- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа. Примеры:

- 6,78 -> 7
- 5 -> нет
- 0,34 -> 3

5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# Seminar 2

Tasks:

1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. Пример:

- Для N = 5: 1, -3, 9, -27, 81

2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

4. Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

5. Данная программа должна вывести n рядов, заполненных знаком "\*" определенным образом. А именно: в первом ряду должно быть n «звездочек», в втором n-1, и так далее. А в последнем ряду таким образом будет одна «звездочка». Причем убывать эти «звездочки» должны слева направо. Число n вводится пользователем.

- Введите количество рядов: 5

   \*\*\*\*\*

  \*\*\*\*

  \*\*\*

  \*\*

  \*

# Seminar 3

Tasks:

1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет. Пример:

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1

# Seminar 5

Tasks:

1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя. Пример:

- [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Seminar 6

Tasks:

1. Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda.

2. Seminar_5\task_3.py

# Seminar 7

Tasks:

Cоздать модульный калькулятор для работы с комплексными и целыми числами(*Пока только с целыми, лень делать проверку на комплексные). Нужно:

- модуль запуска (*start.py*)
- модуль контрллер всех файлов (*controller.py*)
- модуль для для ввода, вывода (*UI.py*)
- модули с математическими операциями (+,-,,/,//,%) - если целые числа | если комплексные - (+,-,,/) (*math_operation.py*)

# My methods

Файл, в котором я собираю все написанные мной методы для того, чтобы в последствии использовать их через импорт.

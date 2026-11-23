# task 2
from math import *

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

n = len(measurements)
total = 0
mn = measurements[0]
mx = measurements[0]
count_chet = 0
count_higher_average = 0

# Этап 1.
for i in range(n):
    total += measurements[i]
    if measurements[i] < mn:
        mn = measurements[i]
    if measurements[i] > mx:
        mx = measurements[i]
    if measurements[i] % 2 == 0:
        count_chet += 1

average = total / n

print('Сумма:', total)
print('Минимум:', mn)
print('Максимум:', mx)
print('Кол-во четных:', count_chet)
print('Среднее:', average)

#  Этап 2. Подсчет значений, превосходящих среднее арифметическое.
for i in range(n):
    if measurements[i] > average:
        count_higher_average += 1
print('Значений выше среднего:', count_higher_average)

# Линейный поиск
number = int(input('Введите число, которое надо найти в списке:' ))
found_index = -1
for i in range(n):
    if measurements[i] == number:
        found_index = i
        break
print('Индекс числа:', found_index)


# Дополнительный алгоритмический эксперимент
deliteli = []
number = int(input('Введите число:'))
for i in range(2, sqrt(n) + 1):
    if n % i == 0:
        deliteli.append(i)





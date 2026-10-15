# Часть 1. Размер отдельных объектов
import sys

empty_list = []
list10 = [0,1,2,3,4,5,6,7,8,9]
tuple10 = (0,1,2,3,4,5,6,7,8,9)
string10 = '0123456789'
number = 10
nothing = None

# === Вывод размеров ===
print("=== Размеры отдельных объектов ===")
print(f'Пустой список:      {sys.getsizeof(empty_list):>4} байт')
print(f'Список из 10 чисел: {sys.getsizeof(list10):>4} байт')
print(f'Кортеж из 10 чисел: {sys.getsizeof(tuple10):>4} байт')
print(f'Строка из 10 чисел: {sys.getsizeof(string10):>4} байт')
print(f'Целое число:        {sys.getsizeof(number):>4} байт')
print(f'None:               {sys.getsizeof(nothing):>4} байт')

#  === Часть 2. Рост списка === 
import sys
data = []
last_size = sys.getsizeof(data)
print("Стартовый размер пустого списка:", last_size, "байт\n")
print(f'{'N':>4} | {'Размер, байт':>12} | {'Прирост':>8}')

for i in range(1,101):
    data.append(i)
    size = sys.getsizeof(data)
    if size != last_size:
        growth = size - last_size
        print(f'{i:>4} | {size:>12} |  {growth:>+8}')
        last_size = size

print('\n Итоговая длина:', len(data))
print('Итоговый размер:', sys.getsizeof(data), 'байт')


#  === Часть 3. Измерение через tracemalloc === 

import tracemalloc

# === Вариант 1: материализованный список ===
tracemalloc.start()
numbers = list(range(100_000))
curr_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("list(range(100_000)):")
print(f"  current: {curr_list/ 1024:.2f} КБ")
print(f"  peak   : {peak_list/ 1024:.2f} КБ")
print()

# === Вариант 2: ленивый range ===
tracemalloc.start()
numbers = range(100_000)
curr_range, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("range(100_000):")
print(f"  current: {curr_range/ 1024:.2f} КБ")
print(f"  peak   : {peak_range/ 1024:.2f} КБ")

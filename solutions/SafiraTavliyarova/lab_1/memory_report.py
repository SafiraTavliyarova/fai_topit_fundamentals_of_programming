# Часть 1. Размер отдельных объектов
print("=" * 78)
print("=== Часть 1. Размеры отдельных объектов ===")
print("=" * 78)

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
print()
print("=" * 78)
print("=== Часть 2. Рост списка ===")
print("=" * 78)

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
print()
print("=" * 78)
print("=== Часть 3. Измерение через tracemalloc ===")
print("=" * 78)
import tracemalloc

# === Вариант 1: материализованный список ===
tracemalloc.start()
numbers1 = list(range(100_000))
curr_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("list(range(100_000):")
print(f"  current: {curr_list/ 1024:.2f} КБ")
print(f"  peak   : {peak_list/ 1024:.2f} КБ")
print()

# === Вариант 2: ленивый range ===
tracemalloc.start()
numbers2 = range(100_000)
curr_range, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("range(100_000)):")
print(f"  current: {curr_range/ 1024:.2f} КБ")
print(f"  peak   : {peak_range/ 1024:.2f} КБ")




# === СВОДНАЯ ТАБЛИЦА ===
print()
print("=" * 78)
print("=== Сводная таблица ===")
print("=" * 78)

headers = ['Сценарий', 'Число элементов', 'Внешний размер', 'Current', 'Peak']
print(f'{headers[0]:<24} {headers[1]:>10} {headers[2]:>14} {headers[3]:>12} {headers[4]:>12}')
print("-" * 78)

print(f"{'Пустой список':<22}: {len(empty_list):>10} {sys.getsizeof(empty_list):>14} байт {'-':>12} {'-':>12}")
print(f"{'Список из 10 чисел':<22}: {len(list10):>10} {sys.getsizeof(list10):>14} байт {'-':>12} {'-':>12}")
print(f"{'Кортеж из 10 чисел':<22}: {len(tuple10):>10} {sys.getsizeof(tuple10):>14} байт {'-':>12} {'-':>12}")
print(f"{'Строка из 10 чисел':<22}: {len(string10):>10} {sys.getsizeof(string10):>14} байт {'-':>12} {'-':>12}")
print(f"{'Целое число':<22}: {'-':>10} {sys.getsizeof(number):>14} байт {'-':>12} {'-':>12}")
print(f"{'None':<22}: {'-':>10} {sys.getsizeof(nothing):>14} байт {'-':>12} {'-':>12}")
print(f"{'list(range(100_000))':<22}: {len(numbers1):>10} {sys.getsizeof(numbers1):>14} байт {curr_list/1024:>12.2f} КБ {peak_list/1024:>12.2f} КБ")
print(f"{'range(100_000)':<22}: {len(numbers2):>10} {sys.getsizeof(numbers2):>14} байт {curr_range/1024:>12.2f} КБ {peak_range/1024:>12.2f} КБ")

# === Oтношение пикового объема двух сравниваемых сценариев ===
print()
print("=" * 78)
print("=== Отношение пикового объёма ===")
print("=" * 78)
print(f'peak(list(range(100_000))) / peak(range(100_000)) =  {peak_list/peak_range:.1f} x')

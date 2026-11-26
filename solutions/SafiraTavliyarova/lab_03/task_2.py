# # task 2
from math import *

# measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

# n = len(measurements)
# total = 0
# mn = measurements[0]
# mx = measurements[0]
# count_chet = 0
# count_higher_average = 0

# # Этап 1.
# for i in range(n):
#     total += measurements[i]
#     if measurements[i] < mn:
#         mn = measurements[i]
#     if measurements[i] > mx:
#         mx = measurements[i]
#     if measurements[i] % 2 == 0:
#         count_chet += 1

# average = total / n

# print('Сумма:', total)
# print('Минимум:', mn)
# print('Максимум:', mx)
# print('Кол-во четных:', count_chet)
# print('Среднее:', average)

# #  Этап 2. Подсчет значений, превосходящих среднее арифметическое.
# for i in range(n):
#     if measurements[i] > average:
#         count_higher_average += 1
# print('Значений выше среднего:', count_higher_average)

# # Линейный поиск
# number = int(input('Введите число, которое надо найти в списке:' ))
# found_index = -1
# for i in range(n):
#     if measurements[i] == number:
#         found_index = i
#         break
# print('Индекс числа:', found_index)


# # Дополнительный алгоритмический эксперимент
# deliteli = []
# n = int(input('Введите положительное целое число:'))
# if n < 2:
#     print("Непростое (число меньше 2)")
# else:
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             deliteli.append(i)
#             if i != n // i:
#                 deliteli.append(n // i)
#     if len(deliteli) == 0:
#         print("Простое")
#     else:
#         print("Непростое")
#         print(f"Делители: {sorted(deliteli)}")



"""Задание 2, практическое расширение: сортировка выбором и поиск."""
# Сортировка выбором + линейный и бинарный поиск со счётчиком сравнений

def selection_sort(values):
    """Сортирует список по возрастанию (сортировка выбором).
    Возвращает новый отсортированный список и число сравнений.
    Исходный список не меняется."""
    arr = values[:]
    n = len(arr)
    comparisons = 0

    for i in range(n - 1):
        # ищем индекс минимального элемента в arr[i:]
        mn_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[mn_idx]:
                mn_idx = j
        arr[mn_idx], arr[i] = arr[i], arr[mn_idx]
    return arr, comparisons

def linear_search(values, target):
    """Ищет target в списке слева направо.
    Возвращает индекс (или -1) и число сравнений."""
    comparisons = 0
    for i in range(len(values)):
        comparisons += 1
        if values[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(values, target):
    """Ищет target в ОТСОРТИРОВАННОМ списке.
    Возвращает индекс (или -1) и число сравнений."""
    left = 0
    right = len(values) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if values[mid] == target:
            return mid, comparisons
        elif values[mid] < target:
            left = mid + 1
        else: # values[mid] > target
            right = mid - 1
    return -1, comparisons



# Проверка алгоритма на n = 10, 100, 1000
# n = 10
data = [9, 3, 7, 1, 5, 2, 8, 4, 6, 10]
sorted_data, sort_cmp = selection_sort(data)
target = sorted_data[-1]
lin_idx, lin_cmp = linear_search(sorted_data, target)
bin_idx, bin_cmp = binary_search(sorted_data, target)
print('Таблица количества выполненных сравнений:')
print("n=10   | линейный", lin_cmp, "  | бинарный", bin_cmp, " | сортировка", sort_cmp)

# n = 100 
data = list(range(100, 0, -1))
sorted_data, sort_cmp = selection_sort(data)
target = sorted_data[-1]
lin_index, lin_cmp = linear_search(sorted_data, target)
bin_index, bin_cmp = binary_search(sorted_data, target)
print("n=100  | линейный", lin_cmp, " | бинарный", bin_cmp, " | сортировка", sort_cmp)


# n = 1000 
data = list(range(1000, 0, -1))
sorted_data, sort_cmp = selection_sort(data)
target = sorted_data[-1]
lin_index, lin_cmp = linear_search(sorted_data, target)
bin_index, bin_cmp = binary_search(sorted_data, target)
print("n=1000 | линейный", lin_cmp, "| бинарный", bin_cmp, "| сортировка", sort_cmp)

print()
print("Поиск ОТСУТСТВУЮЩЕГО элемента:")
for n in (10, 100, 1000):
    data = list(range(n, 0, -1))
    sorted_data, _ = selection_sort(data)
    missing = n + 100
    lin_index, lin_cmp = linear_search(sorted_data, missing)
    bin_index, bin_cmp = binary_search(sorted_data, missing)
    print(f"n={n:<5}| линейный {lin_cmp:<5}| бинарный {bin_cmp}")
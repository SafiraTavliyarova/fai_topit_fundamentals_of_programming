# Эксперимент A. Неизменяемый объект

# a = 10
# b = a

# print(a, b)
# print(id(a), id(b))

# a += 1

# print(a, b)
# print(id(a), id(b))


# Эксперимент B. Изменяемый объект

# first = [10, 20]
# second = first

# print(first, second)
# print(id(first), id(second))

# second.append(30)

# print(first, second)
# print(id(first), id(second))


# # 1. Переназначаем second на НОВЫЙ список с теми же элементами
# second = [10, 20, 30]

# # 2. Сравниваем списки с помощью == и is
# print('first == second:', first == second)
# print('first is second:', first is second)
# print('id(first):', id(first))
# print('id(second):', id(second))


# # 3. Изменяем новый список и проверяем, повлияло ли это на first
# second.append(40)
# print('first:', first)
# print('second:', second)


# Практическая задача
import copy

# === Variant 1: присваивание ===
print('=== Variant 1: присваивание ===')

name_1 = "Project"
people_1 = ['Ivan', 'Michael', 'Nick']
launch_1 = ['arg1', 'arg2']

print("До изменений:")
print("name_1:", name_1)
print("people_1:", people_1)
print("launch_1:", launch_1)

name_2 = name_1
people_2 = people_1
launch_2 = launch_1

assert name_1 is name_2
assert people_1 is people_2
assert launch_1 is launch_2

people_2.append('Olga')
launch_2.append('arg8')

print("После изменений:")
print("people_1:", people_1)
print("people_2:", people_2)
print("launch_1:", launch_1)
print("launch_2:", launch_2)

assert 'Olga' in people_1
assert 'arg8' in launch_1
print(">>> Изменение через people_2/launch_2 затронуло people_1/launch_1 — объекты общие")


# === Variant 2: независимая конфигурация через deepcopy ===
print()
print('=== Variant 2: независимая конфигурация (deepcopy) ===')

name_3 = "Project"
people_3 = ['Ivan', 'Michael', 'Nick']
launch_3 = ['arg1', 'arg2']

print("До изменений:")
print("name_3:", name_3)
print("people_3:", people_3)
print("launch_3:", launch_3)

name_4 = copy.deepcopy(name_3)           
people_4 = copy.deepcopy(people_3)       # глубокое копирование
launch_4 = copy.deepcopy(launch_3)

assert name_3 is name_4                  # общий, но неизменяемый — безопасно
assert people_3 is not people_4
assert launch_3 is not launch_4
assert name_3 == name_4
assert people_3 == people_4
assert launch_3 == launch_4

people_4.append('Olga')
launch_4.append('arg8')

print("После изменений:")
print("people_3:", people_3)
print("people_4:", people_4)
print("launch_3:", launch_3)
print("launch_4:", launch_4)

assert 'Olga' not in people_3
assert 'arg8' not in launch_3
print(">>> people_3 и launch_3 не тронуты — объекты независимы")


# === ИТОГ ===
print()
print('=== ИТОГ ===')

print("Присваивание (=):")
print("  name_1 is name_2:", name_1 is name_2, "(неизменяемый — безопасно)")
print("  people_1 is people_2:", people_1 is people_2)
print("  launch_1 is launch_2:", launch_1 is launch_2)

print("Копирование (deepcopy):")
print("  name_3 is name_4    :", name_3 is name_4, "(неизменяемый — безопасно)")
print("  people_3 is people_4:", people_3 is people_4)
print("  launch_3 is launch_4:", launch_3 is launch_4)
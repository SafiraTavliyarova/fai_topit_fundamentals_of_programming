import gc
# === Цикл из двух списков ===

# first = []
# second = []

# first.append(second)
# second.append(first)

# print("first ссылается на second:", first[0] is second)
# print("second ссылается на first:", second[0] is first)

# # === Состояние сборщика мусора ===
# print('=== Состояние сборщика мусора ===')
# print('\n Автоматический сборщик включён:', gc.isenabled()) # -> True. Если False — автоматика выключена, gc.collect() надо вызывать вручную
# print('Пороги поколений:', gc.get_threshold()) # -> (2000, 10, 0), Что значит: 2000 — в поколении 0 накопилось 2000 объектов с прошлой сборки; 10 — поколение 1 проверялось 10 раз; 0 — поколение 2 не проврялось.
# print('Текущие счётчики поколений:', gc.get_count())
# print('Статистика поколений:', gc.get_stats())

# # === Запоминаем id-ы ===

# id1 = id(first)
# id2 = id(second)
# print('\n id1:', id1)
# print('id2:', id2)


# # === Удаляем имена ===
# del first
# del second
# print("\n Имена first и second удалены")

# # === Запускаем сборщик ===

# gc_collect = gc.collect()
# print('gc.collect() освободил объектов:', gc_collect)


# # ===  дополнительный эксперимент: ===
# import gc
# gc.disable()
# print("Автоматический сборщик отключён:", not gc.isenabled())

# # === Создаем несколько циклических структур ===
# a1 = []
# b1 = []
# a1.append(b1)
# b1.append(a1)

# a2 = []
# b2 = []
# a2.append(b2)
# b2.append(a2)

# a3 = []
# b3 = []
# a3.append(b3)
# b3.append(a3)

# print('\n Создано три цикла')

# del a1, a2, b1, b2, a3, b3
# print('\n Удалили внешние ссылки, остались только циклы')

# print("\n Запускаем gc.collect() вручную")
# collected = gc.collect()
# print("Освобождено объектов:", collected)

# gc.enable()
# print("\n Автоматический сборщик включён обратно:", gc.isenabled())







# Практическая задача
import gc

gc.disable()
print('Автоматический сборщик отключён:', not gc.isenabled())

# === 2. Создаём граф ===
# Узлы A, B, C — в цикле. Узел D — независимый.
A = {'name': 'A', 'links': []}
B = {'name': 'B', 'links': []}
C = {'name': 'C', 'links': []}
D = {'name': 'D', 'links': []}

# Цикл: A → B → C → A. 
A['links'].append(B)
B['links'].append(C)
C['links'].append(A)
# D ни с кем не связан

# === 3. Выводим связи ===
print('\n === Граф ===')
print('A ->', A['links'][0]['name'])
print('B ->', B['links'][0]['name'])
print('C ->', C['links'][0]['name'])
print('D ->',  'нет связей' if not D['links'] else D['links'])

print('\n A сссылается на B:', A['links'][0] is B)
print('B сссылается на C:', B['links'][0] is C)
print('C сссылается на A:', C['links'][0] is A)


# === 4. Считаем сборку ДО удаления графа ===
collected_before = gc.collect()
print("\n gc.collect() до удаления графа:", collected_before)

# === 5. Удаляем внешние имена циклических узлов ===
del A, B, C
print('\n Внешние имена удалены, цикл держит сам себя')

# === 6. Ручная сборка ===
collected_after = gc.collect()
print('\n gc.collect() после удаления графа:', collected_after)


# === 7. Проверяем, что D остался доступен ===
print('\n D доступен', D['name'])
print('D не пуст:', D['links'] == [])

# 8. Включаем обратно автоматический сборщик мусора
gc.enable()
print('\n Автоматический сборщик мусора включен обратно:', gc.isenabled())

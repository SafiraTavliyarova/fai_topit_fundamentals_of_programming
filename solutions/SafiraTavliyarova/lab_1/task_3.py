import sys

# data = [1, 2, 3]
# print("После создания:", sys.getrefcount(data))

# alias = data
# print("После создания alias:", sys.getrefcount(data))

# container = [data]
# print("После помещения в контейнер:", sys.getrefcount(data))

# del alias
# print("После del alias:", sys.getrefcount(data))

# container.clear()
# print("После очистки контейнера:", sys.getrefcount(data))

# Эксперимент со слабой ссылкой

import weakref


# class Record:
#     pass


# record = Record()
# weak_record = weakref.ref(record)

# print(weak_record())
# del record
# print(weak_record())

# === Пример ===
# import weakref

# class channel: # Класс «канал» — тот, кто рассылает что-то подписчикам.
#     def __init__(self): # При создании канала заводим пустой список subs — сюда будем складывать подписчиков.
#         self.subs = []
#     def add(self, x): # Метод «добавить подписчика». Принимает x — объект, который подписывается.
#         self.subs.append(weakref.ref(x))

# class person: # Создаёт объект с именем. Атрибут self.name нужен, чтобы потом можно было печатать, кто получил сообщение.
#     def __init__(self, name):
#         self.name = name

# ch = channel() # Создаём канал. Имя ch — сильная ссылка на него.
# p = person('Alice') # Создаём человека. Имя p — сильная ссылка на него. Счётчик сильных ссылок на Алису = 1.
# ch.add(p) # Передаём p в метод add. Внутри: Параметр x — временная сильная ссылка на Алису (пока выполняется метод).
#           # weakref.ref(x) — создаём слабую ссылку, self.subs.append(...) — кладём слабую ссылку в список канала. 
#           # Метод заканчивается — параметр x исчезает. После этого на Алису ссылается только имя p (сильная) и слабая ссылка в канале (не считается).

# print(ch.subs[0]().name)
# del p # Удаляем сильное имя p. Счётчик сильных ссылок на Алису падает до нуля (слабая ссылка в канале не считается).
# print(ch.subs[0]()) # Алиса удалена → ch.subs[0]() возвращает None.



#  === Практическая задача. Слабый реестр из Record ===

import weakref

class Record: # Объявляет шаблон для объектов
    def __init__(self, name): # Конструктор — вызывается при создании
        self.name = name

    def __repr__(self):
        return f'Record({self.name!r})' # показать объект в виде строки

reestr = weakref.WeakValueDictionary() # Создаём пустой слабый словарь — наш реестр.

r1 = Record('r1') # Сильные ссылки
r2 = Record('r2')

#  Записываем в регистр три объекта
reestr['r1'] = r1
reestr['r2'] = r2
reestr['r3'] = Record('r3') # слабая ссылка. сильных ссылок нет — объект немедленно
                            # удаляется. Запись registry["r3"] сама исчезает.

print('До изменений:', dict(reestr))

del r1
print('После удаления r1:', dict(reestr))

del r2
print('После удаления r2:', dict(reestr))

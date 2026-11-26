# task 3
submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

# 1. Множество всех студентов
students = set()
for name, lab, score in submissions:
    students.add(name)

# 2. Множество всех сданных лабораторных работ.
labs = set()
for name, lab, score in submissions:
    labs.add(lab)

# 3. Словарь: студент -> список попыток (только оценки)
attempts = {}
for name, lab, score in submissions:
    if name not in attempts:
        attempts[name] = []
    attempts[name].append(score)

# 4. Лучший результат по ключу (student, lab)
best = {}
for name, lab, score in submissions:
    key = (name, lab)
    if (key not in best) or (best[key] < score):
        best[key] = score

# 5. Количество попыток по ключу (student, lab)
counts = {}
for name, lab, score in submissions:
    key = (name, lab)
    if key not in counts:
        counts[key] = 1
    else:
        counts[key] += 1

# 6. Студенты, сдававшие ОБЕ работы — через множества
# Для каждой работы — множество студентов, её сдававших
students_by_lab = {}
for name, lab, score in submissions:
    if lab not in students_by_lab:
        students_by_lab[lab] = set()
    students_by_lab[lab].add(name)

# Пересечение множеств студентов по всем работам
both = set(students)  # начинаем со всех
for lab_students in students_by_lab.values():
    both = both & lab_students # пересекаем


# Вывод
print('Студенты:', students)
print('Работы:', labs)
print('Попытки по студентам:', attempts)
print('Лучшие результаты:', best)
print('Количество попыток:', counts)
print('Сдавали обе лабы:', both)



#  Добавление записи
new_record = ("daria", "lab_02", 4)
name, lab, score = new_record

# 1. Множества — просто add (повторы игнорируются)
students.add(name)
labs.add(lab)


# 2. Список попыток — добавляем в конец
#    setdefault(key, default) вернёт существующий список или создаст новый
# С setdefault — 1 строка
attempts.setdefault(name, []).append(score)

## Без setdefault — 3 строки
# if name not in attempts:
#     attempts[name] = []
# attempts[name].append(score)

# 3. Лучший результат — обновляем, только если новый больше
key = (name, lab)
if key not in best or best[key] < score:
    best[key] = score

# 4. Количество попыток — увеличиваем на 1
counts[key] = counts.get(key, 0) + 1

# 5. Множество студентов по работе — добавляем
if lab not in students_by_lab:
    students_by_lab[lab] = set()
students_by_lab[lab].add(name)

# both  — пересчитываем пересечение (это дёшево: работ мало)
both = set(students)
for lab_students in students_by_lab.values():
    both = both & lab_students

submissions.append(new_record)


# Вывод после добавлений
print('')
print('Вывод после добавлений новых записей')
print('Студенты:', students)
print('Работы:', labs)
print('Попытки по студентам:', attempts)
print('Лучшие результаты:', best)
print('Количество попыток:', counts)
print('Сдавали обе лабы:', both)


# ==========================================
# Практическое расширение: текстовые запросы

def handle_query(query_line):
    """Обрабатывает одну текстовую команду и возвращает результат."""
    # Разбиваем строку на слова
    parts = query_line.split()

    # Если ввели пустую строку
    if not parts:
        return 'Ошибка: пустая команда'

    command = parts[0]

    # 1. # 1. student <имя>
    if command == 'student':
        if len(parts) != 2:
            return 'Ошибка: используйте "student <имя>".'
        name = parts[1]
        if name not in attempts:
            return f'Студент <{name}> не найден'
        return f'Попытки студента {name}: {attempts[name]}'

    # 2. best <имя> <работа>
    elif command == 'best':
        if len(parts) != 3:
            return "Ошибка: используйте 'best <имя> <работа>'."
        name = parts[1]
        lab = parts[2]
        key = (name, lab)
        if key not in best:
            return f"Нет данных о лучшем результате для {name} по {lab}."
        return f"Лучший результат {name} по {lab}: {best[key]}"

    # 3. attempts <имя> <работа>
    elif command == 'attempts':
        if len(parts) != 3:
            return "Ошибка: используйте 'attempts <имя> <работа>'."
        name = parts[1]
        lab = parts[2]
        key = (name, lab)
        if key not in counts:
            return f"Нет данных о попытках для {name} по {lab}."
        return f"Количество попыток {name} по {lab}: {counts[key]}"
        
    # 4. completed <работа>
    elif command == 'completed':
        if len(parts) != 2:
            return "Ошибка: используйте 'completed <работа>'."
        lab = parts[1]
        if lab not in students_by_lab:
            return f"Работа {lab} не найдена (никто не сдавал)."
        # Превращаем множество в строку для красивого вывода
        students_list = ', '.join(students_by_lab[lab])
        return f"Работу {lab} сдали: {students_list}"
    
    # Если команда не из списка
    else:
        return f"Неизвестная команда: '{command}'. Доступны: student, best, attempts, completed."


# --- Тестируем запросы ---
print("\n=== ТЕСТИРОВАНИЕ ЗАПРОСОВ ===")

# Список тестовых запросов
queries = [
    "student anna",             # Успешный запрос
    "best anna lab_01",         # Успешный запрос
    "attempts boris lab_02",    # Успешный запрос
    "completed lab_01",         # Успешный запрос
    "student ivan",             # Ошибка: нет такого студента
    "best anna lab_99",         # Ошибка: нет такой работы у студента
    "unknown hello world",      # Ошибка: неизвестная команда
    "student",                  # Ошибка: не хватает аргументов
    ""                          # Ошибка: пустая строка
]


for q in queries:
    print(f'Запрос: {q}')
    print(f"Ответ: {handle_query(q)}\n")
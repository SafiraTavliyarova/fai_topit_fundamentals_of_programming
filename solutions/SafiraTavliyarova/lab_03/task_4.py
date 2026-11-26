# task 4

# 1. Среднее арифметическое
def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    # Если список пустой, возвращаем 0.0 (ранний return, чтобы избежать деления на 0)
    if len(values) == 0:
        return 0.0
    total = 0
    for num in values:
        total += num
    return total / len(values)

# 2. Нормализация имени
def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    # Убираем пробелы в начале и конце. Если ничего не осталось — возвращаем пустую строку.
    if name.strip() == '':
        return ""
    words = name.split()
    clean_words = []
    for word in words:
         # .capitalize() делает первую букву заглавной, а остальные — строчными
        clean_words.append(word.capitalize())
    return ' '.join(clean_words)

# 3. Отчет о результатах
def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if len(results) == 0:
        return f"{prefix} для {student}: нет оценок"

    av = arithmetic_mean(results)
    # Форматируем число. f"{avg:.{precision}f}" означает:
    # вывести avg с точкой и precision знаками после запятой.
    # В синтаксисе f-строк для чисел с плавающей точкой (float)
    # после точки обязательно должна стоять буква f — она означает "float".
    av_text = f'{av:.{precision}f}'
    return f"{prefix}: {student}, средний балл {av_text}"


# 4. Очистка тегов
def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов.
    Что она делает: Очищает теги от мусора (пробелов), приводит к одному регистру и убирает повторы.
    """
    result = []
    # tags — это кортеж всех переданных аргументов
    for tag in tags:
        clean_tag = tag.strip()
        if clean_tag == "":
            continue
        if lowercase == True:
            clean_tag = clean_tag.lower()
        # Добавляем только если такого тега еще нет (проверка на дубликат)
        if clean_tag not in result:
            result.append(clean_tag)
    return tuple(result)


# ==========================================
# ДЕМОНСТРАЦИЯ И ПРОВЕРКИ
# ==========================================


print("--- Тестируем функции ---")
    
# 1. Среднее
print("Среднее [10, 20, 30]:", arithmetic_mean([10, 20, 30]))
assert arithmetic_mean([2, 4, 6]) == 4.0
assert arithmetic_mean([]) == 0.0
assert arithmetic_mean([5]) == 5.0

# 2. Имя
print("Очистка имени:", repr(normalize_name("  иВАН   иВАНОВ ")))
assert normalize_name("  иВАН   иВАНОВ ") == "Иван Иванов"
assert normalize_name("") == ""
assert normalize_name("МАРИЯ") == "Мария"

# 3. Отчет (тут используем precision и prefix как ИМЕНОВАННЫЕ аргументы)
print(build_report("Анна", [85, 90, 95]))
print(build_report("Борис", [70, 75], precision=1, prefix="Отчет"))
    
assert "85.00" in build_report("Анна", [80, 90]) 
assert "85.0" in build_report("Анна", [80, 90], precision=1)
    
# Проверяем, что передать precision просто по порядку НЕЛЬЗЯ
try:
    build_report("Тест", [1, 2], 3)
    assert False, "Должно было упасть"
except TypeError:
    pass # Ожидаемая ошибка

# 4. Теги
print("Теги:", collect_tags("Python", "  python ", "", "Django"))
assert collect_tags("A", " a ", "B") == ("a", "b")
assert collect_tags() == ()


# Распаковка списка через *
my_tags = ["Tag1", "tag2"]
# Это то же самое, что написать collect_tags("Tag1", "tag2")
print('Распаковка *:', collect_tags(*my_tags))

# Распаковка словаря через **
# Ключи в словаре должны точно совпадать с именами параметров функции
my_dict = {
    "student": "Дарья",
    "results": [100, 95],
    "precision": 1
}
# Это то же самое, что build_report("Дарья", [100, 95], precision=1)
print('Распаковка **:', build_report(**my_dict))



# ==========================================
# Исследование LEGB
# ==========================================

print("\n--- Исследование LEGB ---")


# Глобальная область (G)
course = "Питон для начинающих"

def outer_function():
    # Объемлющая область (E)
    teacher = "Иван Петров"
    student_count = 10
    
    def inner_function():
        # Локальная область (L)
        # Мы хотим изменить student_count из внешней функции
        nonlocal student_count
        student_count = student_count + 1
        
        # Читаем глобальную переменную course (менять ее нельзя, поэтому просто читаем)
        return f"Курс: {course}, Преподаватель: {teacher}, Студентов: {student_count}"
        
    # Вызываем вложенную функцию
    result = inner_function()
    print(result)
    
    # Проверяем, изменилась ли переменная во внешней функции
    print("После вызова inner_function, student_count во внешней функции:", student_count)

# Вызываем внешнюю функцию
outer_function()

# Проверяем глобальную переменную (она не должна измениться, если бы мы случайно попытались)
print("Глобальная переменная course осталась:", course)

# - Проверки (assert) -
# Проверяем, что мы не сломали глобальную переменную
assert course == "Питон для начинающих"


# =========
# Ошибка изменяемого значения по умолчанию
# =========

def add_result(value, results=[]):
    results.append(value)
    return results

print(add_result(1))  # Ожидаем [1]. Получаем [1].
print(add_result(2))  # Ожидаем [2]. Получаем [1, 2]!
print(add_result(3))  # Ожидаем [3]. Получаем [1, 2, 3]!


def add_result_fixed(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

# Теперь работает правильно:
print(add_result_fixed(1))  # [1]
print(add_result_fixed(2))  # [2]




# ==========================================
# Практическое расширение
# ==========================================
print("\n--- Функции высшего порядка и замыкания ---")

# --- 1. apply_to_results ---
def apply_to_results(operation, values):
    result = []
    for v in values:
        # operation(v) означает "примени функцию operation к числу v"
        result.append(operation(v))
    return result

# Исходный список
scores = [50, 75, 90]
print(scores)
# 1. Передаем lambda (анонимную функцию "прибавь 5")
print("Lambda (+5):", apply_to_results(lambda x: x + 5, scores))
# Ожидается [55, 80, 95]

print([-10, 5, -20])
# 2. Передаем встроенную функцию abs (модуль числа)
# Она сделает из отрицательных чисел положительные
print("Встроенная abs:", apply_to_results(abs, [-10, 5, -20]))
# Ожидается [10, 5, 20]


# --- 2. make_threshold_checker (Замыкание) ---
def make_threshold_checker(threshold):
    def checker(score):
        return score >= threshold
    return checker

# Создаем две разные проверки (два независимых замыкания)
check_pass = make_threshold_checker(60)       # порог 60
check_excellent = make_threshold_checker(90)  # порог 90

# Проверяем студента с 75 баллами
print("Сдал (порог 60)?", check_pass(75))      # True
print("Отличник (порог 90)?", check_excellent(75)) # False

# Проверяем студента с 95 баллами
print("Отличник (порог 90)?", check_excellent(95)) # True

# Проверки через assert
assert check_pass(60) == True
assert check_pass(59) == False
assert check_excellent(90) == True
assert check_excellent(89) == False

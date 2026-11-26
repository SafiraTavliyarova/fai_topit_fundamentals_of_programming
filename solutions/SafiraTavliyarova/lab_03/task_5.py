# task 5

def mean(values: list) -> float:
    """
    Вычисляет среднее арифметическое списка чисел.
    
    Вход: список чисел (int или float)
    Выход: среднее значение (float)
    Особые случаи: если список пустой — возвращает None
    """
    if len(values) == 0:
        return None
    
    total = 0
    for value in values:
        total += value
    
    return total / len(values)

def minimum(values: list) -> float:
    """
    Находит минимальное значение в списке.
    
    Вход: список чисел (int), не пустой
    Выход: минимальное значение (int)
    Особые случаи: если список пустой — возвращает None
    """
    if len(values) == 0:
        return None
    min_value = values[0]
    for v in values:
        if v < min_value:
            min_value = v
    return min_value



def maximum(values: list) -> float:
    """
    Находит максимальное значение в списке.
    
    Вход: список чисел (int), не пустой
    Выход: максимальное значение (int)
    Особые случаи: если список пустой — возвращает None
    """
    if len(values) == 0:
        return None
    max_value = values[0]
    for v in values:
        if v > max_value:
            max_value = v
    return max_value

def classify(score: float) -> str:
    """
    Определяет текстовую категорию результата.
    
    Вход: числовой результат (float или int) от 0 до 100
    Выход: строка с категорией
    Особые случаи: если score < 0 или > 100 — возвращает "некорректный"
    """
    if score is None:
        return 'нет данных'
    if score < 0 or score > 100:
        return 'некорректный'
    if score >= 90:
        return 'отличный'
    elif score >= 75:
        return 'хороший'
    elif  score >= 60:
        return 'удовлетворительный'
    else:
        return 'недостаточный'


def student_summary(name: str, results: list) -> dict:
    """
    Формирует словарь с итогами одного студента.
    
    Вход: имя студента (str), список результатов (list)
    Выход: словарь с ключами: name, mean, min, max, category
    """
    av = mean(results)

    return {
        "name": name,
        "mean": av,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(av)
    }

def group_summary(students: dict) -> dict:
    """
    Формирует общую статистику группы.
    
    Вход: словарь {имя: [результаты]}
    Выход: словарь с ключами: total_students, category_counts, group_mean
    """
    category_counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
        "нет данных": 0
    }

    all_means = []
    for name, values in students.items():
        av = mean(values)
        if av is not None:
            all_means.append(av)
        category = classify(av)
        if category in category_counts:
            category_counts[category] += 1

    if len(all_means) != 0:
        group_mean = mean(all_means)
    else:
        group_mean = None
    return {
        "total_students": len(students),
        "category_counts": category_counts,
        "group_mean": group_mean
    }

def find_top_students(students: dict) -> list:
    """
    Находит студентов с наибольшим средним результатом.
    
    Вход: словарь {имя: [результаты]}
    Выход: список имён студентов-лидеров
    """
    if len(students) == 0:
        return []

    averages = {}
    for name, results in students.items():
        av = mean(results)
        if av is not None:
            averages[name] = av
    if len(averages) == 0:
        return []
    
    # Находим максимальный средний балл
    max_av = maximum(list(averages.values()))
    # Собираем всех студентов с этим баллом
    top_students = []
    for name, avg in averages.items():
        if avg == max_av:
            top_students.append(name)
    return top_students

def format_report(student_data: list, group_data: dict) -> str:
    """
    Формирует текстовый отчёт.
    
    Вход: список словарей со статистикой студентов, словарь со статистикой группы
    Выход: строка с отчётом
    """
    report = "=== ОТЧЁТ ПО ГРУППЕ ===\n\n"
    
    # Индивидуальные результаты

    report += "--- Индивидуальные результаты ---\n"
    for student in student_data:
        report += f"Студент: {student['name']}\n"

        mean_val = student['mean']
        if mean_val is not None:
            report += f"  Средний балл: {mean_val:.2f}\n"
            report += f"  Минимум: {student['min']}\n"
            report += f"  Максимум: {student['max']}\n"
        else:
            report += "  Средний балл: нет данных\n"
            report += "  Минимум: нет данных\n"
            report += "  Максимум: нет данных\n"
        report += f"  Категория: {student['category']}\n\n"

    # Общая статистика
    report += "--- Общая статистика ---\n"
    report += f"Всего студентов: {group_data['total_students']}\n"
    group_mean = group_data['group_mean']
    if group_mean is not None:
        report += f"Средний балл группы: {group_mean:.2f}\n\n"
    else:
        report += "Средний балл группы: нет данных\n\n"
    # Распределение по категориям
    report += "--- Распределение по категориям ---\n"
    for category, count in group_data['category_counts'].items():
        report += f"{category}: {count}\n"

    return report
        


# Исходные данные
# students = {
#     "Анна": [78, 91, 84, 88],
#     "Борис": [60, 72, 68],
#     "Дарья": [95, 93, 97, 90],
#     "Илья": [55, 61],
#     "Елена": [],  # студент без результатов
# }


# # Тестовые сценарии
# 1. Обычный набор данных
# students = {
#     "Анна": [78, 91, 84, 88],
#     "Борис": [60, 72, 68],
# }
# # 2. Один студент
# students = {
#     "Анна": [85, 90, 88],
# }
# 3. Несколько лидеров (среднее 90)
# students = {
#     "Анна": [90, 90],
#     "Борис": [85, 95],
# }
# 4. Пустая группа
students = {}
# # 5. Студент без результатов
# students = {
#     "Анна": [85, 90],
#     "Елена": [],
# }
# # 6. Граничные значения категорий
# students = {
#     "Отличник": [90],
#     "Хорошист": [75],
#     "Удовл": [60],
#     "Неуд": [59],
# }


 # Формируем статистику по каждому студенту
student_summaries = []
for name, results in students.items():
    summary = student_summary(name, results)
    student_summaries.append(summary)
    
# Формируем общую статистику группы
group_data = group_summary(students)
    
# Находим лидеров
top_students = find_top_students(students)
print(f"Лидеры группы: {', '.join(top_students)}\n")
    
# Формируем и выводим отчёт
report = format_report(student_summaries, group_data)
print(report)

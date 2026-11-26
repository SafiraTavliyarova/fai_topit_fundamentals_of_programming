# #"""Часть 1""" При практическом задании закомментить !
# def check_input(score, type_of_work, missed):
#     # Проверка диапазонов
#     if score < 0 or score > 100:
#         print('Ошибка: результат должен быть в диапазоне от 0 до 100.')
#         is_valid = False
#     elif type_of_work not in ('exam', 'project', 'practice'):
#         print('Ошибка: тип работы должен быть exam, project или practice.')
#         is_valid = False
#     elif missed < 0 or missed > 5:
#         print('Ошибка: количество пропущенных занятий должно быть в диапазоне от 0 до 5.')
#         is_valid = False
#     else:
#         is_valid = True
#     return is_valid


"""Часть 2. Определение уровня результата."""
def get_level(score, missed):
    if 90 <= score <= 100:
        level = 'отличный'
    elif 75 <= score <= 89:
        level = 'хороший'
    elif 60 <= score <= 74:
        level = 'удовлетворительный'
    else:
        level = 'недостаточный'

    # Снижение уровня при пропусках
    if missed > 3 and level != 'недостаточный':
        if level == 'отличный':
            level = 'хороший'
        elif level == 'хороший':
            level = 'удовлетворительный'
        elif level == 'удовлетворительный':
            level = 'недостаточный'

    return level


"""Часть 3. Сопоставление с образцом (match / case)."""
def get_work_description(type_of_work):
    match type_of_work:
        case 'exam':
            return 'экзаменационная работа'
        case 'project':
            return 'проектная работа'
        case 'practice':
            return 'практическая работа'
        case _:
            return 'неизвестный тип работы'



# Практическое расширение

def check_input(score, type_of_work, missed):
    # Проверка диапазонов
    if score < 0 or score > 100:
        return False
    elif type_of_work not in ('exam', 'project', 'practice'):
        return  False
    elif missed < 0 or missed > 5:
        return False
    else:
        return True


def process_students_list(students):
    results = []

    level_counts = {
        'отличный': 0,
        'хороший': 0,
        'удовлетворительный': 0,
        'недостаточный': 0,
    }

    for student in students:
        score, work_type, missed = student

        # Проверяем корректность
        if not check_input(score, work_type, missed):
            results.append(f'Студент ({score}, {work_type}, {missed}): ОШИБКА ВВОДА')
            continue

        level = get_level(score, missed)
        description = get_work_description(work_type)

        # Формируем строку результата
        result_line = f'Результат: {score}, Тип: {description}, Пропусков: {missed} → Уровень: {level}'
        results.append(result_line)

        level_counts[level] += 1

    # ВОЗВРАЩАЕМ данные
    return results, level_counts


# Список студентов
students_data = [
    (0,   "exam", 0),
    (59,  "exam", 0),
    (74,  "exam", 0),
    (89,  "exam", 0),
    (95, "exam", 2),
    (88, "project", 1),
    (72, "practice", 4),
    (60, "exam", 0),
    (55, "project", 2),
    (100, "exam", 0),
    (90, "practice", 5),
    (75, "exam", 3),
    (80, "project", 4),
    (45, "practice", 1),
    (101, "exam", 0),     # ошибка: результат вне диапазона
    (85, "test", 2),      # ошибка: неизвестный тип работы
]


def main():
    """Главная функция программы."""
    print("\n=== Практическое расширение: Обработка списка студентов ===\n")
    
    # Вызываем функцию и сохраняем результат в переменные
    results_list, counts_dict = process_students_list(students_data)
    
    # Выводим индивидуальные результаты
    print("--- ИНДИВИДУАЛЬНЫЕ РЕЗУЛЬТАТЫ ---")
    for line in results_list:
        print(line)
    
    # Выводим итоговую сводку
    print("\n--- ИТОГОВАЯ СВОДКА ---")
    for level, count in counts_dict.items():
        print(f"{level}: {count} студент(ов)")


if __name__ == "__main__":
    main()
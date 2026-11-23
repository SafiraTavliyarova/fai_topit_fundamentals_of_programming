#########
import random 
# def generate_worst_case(n):
#     """Наихудший случай: массив отсортирован в обратном порядке"""
#     return list(range(n, , -1))

# def generate_best_case(n):
#     """Наилучший случай: массив уже отсортирован"""
#     return list(range(1, n + 1))

# def generate_random_case(n):
#     """Средний случай: случайный массив"""
#     arr = list(range(1, n + 1))
#     random.shuffle(arr)
#     return arr


# k = 0
# arr = []
# for i in range(10**9,0, -1):
#     arr.append(int(i))
#     k += 1
#     if k == 1000:
#         break
# print(len(arr))
# print(*arr)

# print(20)
# print(*random.sample(range(1, 100), 20))




import random
import os
import time

def generate_max_test(filename='input_task2_max.txt', m=1_000_000):
    print(f"Начинаю генерацию {m} команд...")
    start_time = time.time()
    
    # Открываем файл для записи в папке, где лежит скрипт
    with open(filename, 'w') as f:
        # Записываем количество команд
        f.write(f"{m}\n")
        
        adds = m // 2  # 500 000 добавлений
        removes = m - adds  # 500 000 извлечений
        
        # Генерируем добавления
        for _ in range(adds):
            # Числа от 1 до 10^9
            number = random.randint(1, 10**9)
            f.write(f"+ {number}\n")
            
        # Генерируем извлечения
        for _ in range(removes):
            f.write("-\n")
            
    end_time = time.time()
    
    # Получаем полный путь к файлу, чтобы показать пользователю
    full_path = os.path.abspath(filename)
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    
    print("=" * 40)
    print("✅ ГЕНЕРАЦИЯ ЗАВЕРШЕНА!")
    print(f"📁 Файл сохранен по пути: \n{full_path}")
    print(f"📦 Размер файла: {size_mb:.2f} МБ")
    print(f"⏱  Время генерации: {end_time - start_time:.2f} секунд")
    print("=" * 40)

if __name__ == '__main__':
    generate_max_test()
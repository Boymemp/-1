# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:  # Открываем JSON файл:
        data = json.load(file)  # Загружаем данные из файла

    total_sum = 0  # Переменная для хранения суммы произведений

    for entry in data:  # Проходим по каждому словарю в загруженных данных
        # Извлекаем значения "score" и "weight":
        score = entry.get("score", 0)  # По умолчанию 0, если ключа нет
        weight = entry.get("weight", 0)  # По умолчанию 0, если ключа нет
        # Увеличиваем сумму на произведение score и weight:
        total_sum += score * weight
    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)

print(task())

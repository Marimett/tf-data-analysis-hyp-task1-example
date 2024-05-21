import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 361109448

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    # Пропорции успехов в контрольной и тестовой группах
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Объединенная пропорция успехов
    p = (x_success + y_success) / (x_cnt + y_cnt)
    
    # Стандартное отклонение объединенной пропорции
    se = np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    
    # Z-значение
    z = (p1 - p2) / se
    
    # Критическое значение для уровня значимости 0.05 (двусторонний тест)
    z_critical = norm.ppf(1 - 0.05 / 2)
    
    # Проверка гипотезы: возвращаем True, если абсолютное значение z больше критического значения
    return abs(z) > z_critical

# Пример кода для импорта данных из CSV
def main():
    # Укажите путь к вашему CSV-файлу
    csv_file_path = 'hist_telesales.csv'
    
    try:
        # Загружаем данные из CSV-файла
        data = pd.read_csv(csv_file_path)
        
        # Разделяем данные на две группы. В данном случае мы будем использовать деление по ID (например, четные и нечетные ID)
        group1 = data[data['ID'] % 2 == 0]
        group2 = data[data['ID'] % 2 == 1]
        
        # Подсчитываем x_success, x_cnt, y_success, y_cnt
        x_success = group1['Флаг продажи'].sum()
        x_cnt = group1['Флаг дозвона'].sum()
        y_success = group2['Флаг продажи'].sum()
        y_cnt = group2['Флаг дозвона'].sum()
        
        # Выводим подсчитанные значения для проверки
        print(f"x_success: {x_success}, x_cnt: {x_cnt}, y_success: {y_success}, y_cnt: {y_cnt}")
        
        # Вызываем функцию solution
        result = solution(x_success, x_cnt, y_success, y_cnt)
        print("Результат проверки гипотезы:", result)
    except FileNotFoundError:
        print(f"Файл {csv_file_path} не найден.")
    except pd.errors.EmptyDataError:
        print("CSV-файл пуст.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск основного кода
if __name__ == "__main__":
    main()


# In[ ]:





import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 361109448 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Пропорции успехов в контрольной и тестовой группах
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Стандартное отклонение объединенной пропорции
    se = np.sqrt(p1*(1-p1)/x_cnt + p2*(1-p2)/y_cnt)
    
    # Z-значение
    z = (p1 - p2) / se
    
    # Критическое значение для уровня значимости 0.05 (двусторонний тест)
    z_critical = norm.ppf(1 - 0.05 / 2)
    
    # Проверка гипотезы: возвращаем True, если абсолютное значение z больше критического значения
    return abs(z) > z_critical

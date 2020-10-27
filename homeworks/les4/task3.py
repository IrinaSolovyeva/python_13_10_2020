"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
def my_range(start, stop, step):
    """Арифметическая прогрессия от start до stop с шагом step

    :param start: первое значение
    :param stop: последнее значение
    :param step: шаг
    :return:
    """
    list_range = []
    while start < stop:
        list_range.append(start)
        start += step
    return list_range

new_list = [el for el in my_range(20, 240, 1) if (el % 20 == 0 or el % 21 == 0)]
print(f"Список: {new_list}")

"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

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

def my_func(prev_el, el):
    """
    :param prev_el: предыдущий элемент
    :param el: текущий элемент
    :return:
    """
    return prev_el * el

new_list = [el for el in my_range(100, 1001, 1) if el % 2 == 0]
print(f"Список: {new_list}")
print(f"Результат: {reduce(my_func, new_list)}")

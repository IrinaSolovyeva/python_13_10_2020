"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
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

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[itm + 1] for itm in my_range(0, len(my_list)-1, 1) if my_list[itm + 1] > my_list[itm]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

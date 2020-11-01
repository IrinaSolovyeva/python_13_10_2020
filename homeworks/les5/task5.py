"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

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

def sum_array(term):
    """Возвращает сумму элементов массива

    :param term: массив
    :return: сумма элементов
    """
    my_sum = 0
    for i in my_range(0, len(term), 1):
        my_sum += int(term[i])
    return my_sum

numbers = [random.randint(1, 100) for i in range(50)]

with open("task5.txt", "w", encoding="UTF-8") as my_file:
    for itm in numbers:
        my_file.write(str(itm) + " ")

with open("task5.txt", "r", encoding="UTF-8") as my_file:
    content = my_file.read()
    numbers_list = content.split()

print(f"Сумма чисел = {sum_array(numbers_list)}")

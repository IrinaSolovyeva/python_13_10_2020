"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_max(mas):
    """
    Возвращает максимальный элемент.
    """
    maximum = mas[0]
    for i in range(1, len(mas)):
        if mas[i] > maximum:
            maximum = mas[i]
    return maximum

def my_func(arg_1, arg_2, arg_3):
    """
    Возвращает сумму наибольших двух аргументов из трех введенных
    """
    try:
        var_1 = float(arg_1)
        var_2 = float(arg_2)
        var_3 = float(arg_3)
    except ValueError:
        return print("Введите числа")

    var_list = [var_1, var_2, var_3]
    max1 = my_max(var_list)
    var_list.remove(max1)
    max2 = my_max(var_list)
    return max1 + max2

print(my_func(88, 8.4, 4))

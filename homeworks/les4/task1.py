"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, my_output, my_rate, my_bonus = argv

def salary(output, rate, bonus):
    """Расчет заработной платы сотрудника

    :param output: выработка в часах
    :param rate: ставка в час
    :param bonus: премия
    :return:
    """
    result = int(output) * float(rate) + float(bonus)
    return result

print(f"Заработная плата сотрудника = {salary(my_output, my_rate, my_bonus)}")

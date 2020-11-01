"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
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

def average(term, count):
    """Возвращает среднее арифметическое элементов массива

    :param term: массив
    :param count: количество элементов массива
    :return: сумма элементов, деленная на их количество
    """
    my_sum = 0
    for i in my_range(0, count, 1):
        my_sum += term[i]
    return my_sum / count

my_dict = {}
result_list = []
worker_list = []
worker_salary = []
salary_level = 12000

with open("task3.txt", "r", encoding="UTF-8") as my_file:
    for line in my_file:
        my_list = line.split()
        my_dict = {"Фамилия": my_list[0], "Зарплата": float(my_list[1])}
        result_list.append(my_dict)
    for dict_itm in result_list:
        if dict_itm.get("Зарплата") < salary_level:
            worker_list.append(dict_itm.get("Фамилия"))
        worker_salary.append(dict_itm.get("Зарплата"))
    print(f"У данных сотрудников зарплата меньше {salary_level} рублей:")
    for itm in worker_list:
        print(itm)
    salary = average(worker_salary, len(worker_salary))
    print(f"Средняя величина дохода сотрудников: {salary} рублей")

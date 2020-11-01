"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

firm_dict = {}
firm_profit_dict = {}
sum_profit = 0
average_dict = {}
with open("task7.txt", "r", encoding="UTF-8") as my_file:
    for line in my_file:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        firm_dict.update({line[0]: profit})
        if profit >= 0:
            firm_profit_dict.update({line[0]: profit})
            sum_profit += profit
        average_profit = sum_profit / len(firm_profit_dict.values())

average_dict = {'average_profit': average_profit}
result_list = [firm_dict, average_dict]

with open('task7.json', 'w', encoding='UTF-8') as json_file:
    json.dump(result_list, json_file)

"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
profit = float(input("Введите выручку фирмы - "))
costs = float(input("Введите издержки фирмы - "))
if profit >= costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила - {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы - "))
    print(f"Прибыль в расчете на одного сторудника сотавила - {profit / workers:.2f}")
else:
    print("Фирма работает в убыток")

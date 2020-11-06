"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

worker1 = Position("Алексей", "Иванов", "Экономист", 12700, 1000)
print(f"Имя: {worker1.name}")
print(f"Фамилия: {worker1.surname}")
print(f"Должность: {worker1.position}")
print(f"У сотрудника {worker1.get_full_name()} доход {worker1.get_total_income()}")

worker2 = Position("Михаил", "Петров", "Дизайнер", 13000, 500)
print(f"Имя: {worker2.name}")
print(f"Фамилия: {worker2.surname}")
print(f"Должность: {worker2.position}")
print(f"У сотрудника {worker2.get_full_name()} доход {worker2.get_total_income()}")

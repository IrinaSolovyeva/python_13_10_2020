"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title
        print("Вы используете канцелярские принадлежности")

    def draw(self):
        print(f"У вас в руках {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"У вас в руках {self.title}\n")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"У вас в руках {self.title}\n")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"У вас в руках {self.title}\n")

pen1 = Pen("Ручка")
pen1.draw()
pencil1 = Pencil("Карандаш")
pencil1.draw()
handle1 = Handle("Маркер")
handle1.draw()

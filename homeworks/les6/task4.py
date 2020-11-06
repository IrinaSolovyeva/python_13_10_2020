"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 100
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"и остановилась")

    def turn(self, direction):
        print(f"повернула на {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.name} составляет {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение допустимой скорости  60 км/ч")

class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение допустимой скорости 40 км/ч")

class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)

mini = TownCar("красная", "Mini")
mini.go()
mini.turn("лево")
mini.stop()
mini.show_speed()
print(f"Машина {mini.name} {mini.color}")
print(f"Проверка принадлежности к рядам полиции {mini.is_police}\n")

audi = SportCar("белая", "Audi")
audi.go()
audi.turn("право")
audi.stop()
audi.show_speed()
print(f"Машина {audi.name} {audi.color}")
print(f"Проверка принадлежности к рядам полиции {audi.is_police}\n")

ford = WorkCar("серая", "Ford")
ford.go()
ford.turn("право")
ford.stop()
ford.show_speed()
print(f"Машина {ford.name} {ford.color}")
print(f"Проверка принадлежности к рядам полиции {ford.is_police}\n")

dodge = PoliceCar("черная", "Dodge")
dodge.go()
dodge.turn("право")
dodge.stop()
dodge.show_speed()
print(f"Машина {dodge.name} {dodge.color}")
print(f"Проверка принадлежности к рядам полиции {dodge.is_police}\n")

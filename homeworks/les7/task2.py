"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, width):
        self.V = float(width)

    @property
    def consumption(self):
        result = self.V / 6.5 + 0.5
        print(f"Расход ткани на пальто: %.2f" % result)
        return result

class Jacket(Clothes):
    def __init__(self, hight):
        self.H = float(hight)

    @property
    def consumption(self):
        result = 2 * self.H + 0.3
        print(f"Расход ткани на костюм: %.2f" % result)
        return result

if __name__ == '__main__':
    coat = Coat(2)
    jacket = Jacket(4)
    print(f"Суммарный расход ткани: %.2f" % (coat.consumption + jacket.consumption))

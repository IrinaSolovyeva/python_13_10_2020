"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber((self.real + other.real), (self.imag + other.imag))

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imag * other.imag),
                             (self.imag * other.real) + self.real * other.imag)

x1 = ComplexNumber(1, 2)
print(x1)
x2 = ComplexNumber(3, 4)
print(x2)
print(x1.__add__(x2))
print(x1.__mul__(x2))

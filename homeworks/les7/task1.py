"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:
    def __init__(self, m_content):
        self.m_content = m_content

    def __str__(self):
        for i in range(len(self.m_content)):
            for j in range(len(self.m_content[i])):
                print(f"% 3d" % self.m_content[i][j], end=" ")
            print()
        return " "

    def __getitem__(self, index):
        return self.m_content[index]

    def __add__(self, other):
        for i in range(len(self.m_content)):
            for j in range(len(self.m_content[i])):
                print(f"% 3d" % (self.m_content[i][j] + other.m_content[i][j]), end=" ")
            print()
        return " "

if __name__ == '__main__':
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    b = Matrix([[7, 8, 9], [10, 11, 12]])
    print(b)
    c = a + b
    print(c)

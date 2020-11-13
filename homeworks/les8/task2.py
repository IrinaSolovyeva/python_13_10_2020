"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""
class OwnDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_division():
    try:
        var_1 = float(input("Введите первое число (делимое): "))
        var_2 = float(input("Введите второе число (делитель): "))
        if var_2 == 0:
            raise OwnDivision("Делитель не может быть нулем")
        result = var_1 / var_2
    except ValueError:
        print("Вы ввели не число")
    except OwnDivision as err:
        print(err)
    else:
        print(f"Все хорошо. Результат деления двух чисел: %.2f" % result)
    return

my_division()

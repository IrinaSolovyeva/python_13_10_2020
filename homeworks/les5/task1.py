"""
 Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""
line = " "
with open("task1.txt", "w", encoding="UTF-8") as my_file:
    while line:
        line = input("Введите новую строку: ") + "\n"
        if line == "\n":
            break
        my_file.writelines(line)

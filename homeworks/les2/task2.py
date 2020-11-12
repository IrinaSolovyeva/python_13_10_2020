"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

"""Вариант 1 - ввод данных"""

user_text = input("Введите список значений через пробел - ")
user_list = user_text.split()
list_item = 0

"""
Вариант 2 - ввод данных

user_count = int(input("Введите количество элементов в списке - "))
count = 0
user_list = []
while count < user_count:
    user_text = input("Введите значение - ")
    user_list.append(user_text)
    count += 1
"""

print("Ваш список:\n", user_list)

"""
Вариант 1 - обмен значений

for range_item in range(len(user_list)//2):
    user_list[list_item], user_list[list_item + 1] = user_list[list_item + 1], user_list[list_item]
    list_item += 2
"""

"""Вариант 2  - обмен значений"""

for range_item in range(1, len(user_list), 2):
    user_list[list_item], user_list[list_item + 1] = user_list[list_item + 1], user_list[list_item]
    list_item += 2
print("Новый список:\n", user_list)

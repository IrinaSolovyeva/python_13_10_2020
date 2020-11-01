"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dict_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_list = []
result_list = []
with open("task4_1.txt", "r", encoding="UTF-8") as file_info:
    for line in file_info:
        my_list = line.split(" — ")
        new_list = dict_words.get(my_list[0]) + " — " + my_list[1]
        result_list.append(new_list)

with open("task4_2.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(result_list)

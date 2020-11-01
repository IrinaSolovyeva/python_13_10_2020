"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("task2.txt", "r", encoding="UTF-8") as my_file:
    lines = 0
    for idx, line in enumerate(my_file, 1):
        line = line.split()
        count_words = len(line)
        lines += 1
        print(f"В {idx} строке {count_words} слов")
    print(f"Всего {lines} строк")

"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

list_season = ["зима", "весна", "лето", "осень"]
dict_season = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима"
}
while True:
    user_month = input("Введите месяц по номеру - ")
    if user_month.isdigit():
        num = int(user_month)
        break
    print("Необходимо ввести число, а не текст")
if num == 1 or num == 12 or num == 2:
    print(list_season[0])
    print(dict_season.get(num))
elif num == 3 or num == 4 or num == 5:
    print(list_season[1])
    print(dict_season.get(num))
elif num == 6 or num == 7 or num == 8:
    print(list_season[2])
    print(dict_season.get(num))
elif num == 9 or num == 10 or num == 11:
    print(list_season[3])
    print(dict_season.get(num))
else:
    print("Необходимо ввести число от 1 до 12")

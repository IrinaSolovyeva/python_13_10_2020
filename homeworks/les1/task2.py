"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_seconds = int(input("Введите время в секундах - "))
hours = user_seconds // 3600
minutes = (user_seconds // 60) % 60
seconds = user_seconds % 60
if minutes < 10:
    minutes = str("0" + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str("0" + str(seconds))
else:
    seconds = str(seconds)
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

user_name = input("Введите имя - ")
user_surname = input("Введите фамилию - ")
user_bday = input("Введите год рождения - ")
user_city = input("Введите город проживания - ")
user_email = input("Введите email - ")
user_phone = input("Введите телефон - ")

def info_person(name, surname, bday, city, email, phone):
    """
    Выполняет обработку данных пользователя и выводит данные одной строкой.
    """
    print(f"Имя - {name}. Фамилия - {surname}. Год рождения - {bday}. Город проживания - {city}. email - {email}. Телефон - {phone}")

info_person(name=user_name, surname=user_surname, bday=user_bday, city=user_city, email=user_email, phone=user_phone)

from datetime import datetime


def check_date_input_year(element):
    """Checks whether the input is correctly formated"""
    date = input('Введіть дедлайн формату (2021-11-01 12:37:00).\n' + element + ': ')
    while True:
        if date.isdigit() and len(date) == 4:
            return date
        else:
            date = input('Некорректний формат, очікується 4 цифри.\n' + element + ': ')


def check_date_input_month(element):
    """Checks whether the input is correctly formated"""
    date = input('Введіть дедлайн формату (2021-11-01 12:37:00).\n' + element + ': ')
    while True:
        if date.isdigit() and len(date) == 2 and int(date) <= 12:
            return date
        else:
            date = input('Некорректний формат, очікується 2 цифри, місяців всього 12.\n' + element + ': ')


def check_date_input_day(element):
    """Checks whether the input is correctly formated"""
    date = input('Введіть дедлайн формату (2021-11-01 12:37:00).\n' + element + ': ')
    while True:
        if date.isdigit() and len(date) == 2 and int(date) <= 31:
            return date
        else:
            date = input('Некорректний формат, очікується 2 цифри, у місяці не більше 31 дня.\n' + element + ': ')


def check_date_input_hour(element):
    """Checks whether the input is correctly formated"""
    date = input('Введіть дедлайн формату (2021-11-01 12:37:00).\n' + element + ': ')
    while True:
        if date.isdigit() and len(date) == 2 and int(date) <= 23:
            return date
        else:
            date = input('Некорректний формат, очікується 2 цифри, у дні 24 години.\n' + element + ': ')


def check_date_input_minute(element):
    """Checks whether the input is correctly formated"""
    date = input('Введіть дедлайн формату (2021-11-01 12:37:00).\n' + element + ': ')
    while True:
        if date.isdigit() and len(date) == 2 and int(date) <= 59:
            return date
        else:
            date = input('Некорректний формат, очікується 2 цифри, у годині 60 хвилин.\n' + element + ': ')


def ask_datetime():
    """Asks user to input date"""
    year = check_date_input_year('Рік')
    month = check_date_input_month('Місяць')
    day = check_date_input_day('День')
    hour = check_date_input_hour('Година')
    minute = check_date_input_minute('Хвилина')
    deadline = datetime(int(year), int(month), int(day), int(hour), int(minute))
    return deadline
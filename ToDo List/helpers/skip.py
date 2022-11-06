from source.clear_screen import cls


def skip():
    answer = input("Введіть 'y', щоб побачити функції прграмми: ")
    while True:
        if answer.lower() == 'y':
            cls()
            break
        else:
            answer = input('Введіть корректний символ: ')
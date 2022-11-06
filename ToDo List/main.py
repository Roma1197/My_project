from source import *
from helpers import *
from data.test_data import TASK_TEST, tasks
import os
import json

# load_json_tasks.import_json_file('data', 'tasks.json') Не вдається завантажити данні у програму, після виконання функції ліст tasks чомусь залишається пустим.
# print(tasks)

cwd = os.getcwd()
dir_path = os.path.join(cwd, 'data', 'tasks.json')
try:
    with open(dir_path, 'r') as my:
        get = my.read()
        tasks = json.loads(get)
except FileNotFoundError:
    print('Файл з задачами відсутній.')

convert_str_to_datetime.convert_str_to_datetime(tasks)

print('Доступні функції:')

for index in functional.functions:
    print(index + ': ' + functional.functions[index])

chosen = input('Виберіть функцію та введіть відповідну букву: ')
while True:
    if chosen.lower() == 'm':
        clear_screen.cls()
        convert_datetime_to_str.convert_datetime_to_str(tasks)
        save_as_json.save_as_json('data', 'tasks.json', tasks)
        print('Данні збережено. До зустрічі!')
        break
    elif chosen.lower() in functional.answer_option:
        if chosen.lower() == 'a':
            clear_screen.cls()
            add_task.add_new_task(tasks)
            print(tasks)
            skip.skip()
        elif chosen.lower() == 'b':
            clear_screen.cls()
            find_task.find_task(tasks)
            skip.skip()
        elif chosen.lower() == 'c':
            clear_screen.cls()
            find_change_done.change_done_status(tasks)
            skip.skip()
        elif chosen.lower() == 'd':
            clear_screen.cls()
            find_change_priority.change_priority(tasks)
            skip.skip()
        elif chosen.lower() == 'e':
            clear_screen.cls()
            remove_task.del_task(tasks)
            skip.skip()
        elif chosen.lower() == 'f':
            clear_screen.cls()
            check_tasks_adding_order.check_order(tasks)
            skip.skip()
        elif chosen.lower() == 'g':
            clear_screen.cls()
            check_tasks_priority_order.check_priority(tasks)
            skip.skip()
        elif chosen.lower() == 'h':
            clear_screen.cls()
            check_uncompleted.check_uncompleted(tasks)
            skip.skip()
        elif chosen.lower() == 'i':
            clear_screen.cls()
            check_completed.check_completed(tasks)
            skip.skip()
        elif chosen.lower() == 'j':
            clear_screen.cls()
            check_overdue.check_overdue(tasks)
            skip.skip()
        elif chosen.lower() == 'k':
            clear_screen.cls()
            check_statistics.check_stat(tasks)
            skip.skip()
        elif chosen.lower() == 'l':
            clear_screen.cls()
            convert_datetime_to_str.convert_datetime_to_str(tasks)
            save_as_csv.save_as_csv('data', 'tasks.csv', tasks)
            print('Тестові данні збережено.')
            skip.skip()
        for index in functional.functions:
            print(index + ': ' + functional.functions[index])
        chosen = input('Виберіть функцію та введіть відповідну букву: ')
    else:
        chosen = input('Виберіть корректний індекс задачі: ')
from data.test_data import tasks
from helpers.ask_date import ask_datetime


def ask(name):
    """Asks user to input str"""
    key = input('Введіть ' + name + ': ')
    return key


def ask_digit(name):
    """Asks user to input int"""
    key = input('Введіть ' + name + ': ')
    while True:
        if key.isdigit():
            return key
        else:
            key = input('Enter the digit, please: ')


def add_new_task(tasks_pool):
    """This will add a task to the pool"""
    task = {}
    task['id'] = len(tasks) + 1
    get_title = ask('коротку назву справи')
    task['title'] = get_title[:50]
    task['description'] = ask('детальний опис (не обов\'язково)')
    if not task['description']:
        task['description'] = task['title']
    get_priority = ask_digit('пріорітет задачі від 1 до 10')
    if len(get_priority) > 10:
        task['priority'] = 10
    else:
        task['priority'] = get_priority
    task['due_date'] = ask_datetime()
    task['done'] = False
    tasks_pool.append(task)
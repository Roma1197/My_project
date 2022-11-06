from datetime import datetime


def count_uncompleted(tasks_pool):
    n = 0
    for element in tasks_pool:
        if element['done'] is False:
            n += 1
    return n


def count_completed(tasks_pool):
    n = 0
    for element in tasks_pool:
        if element['done']:
            n += 1
    return n


def count_overdue(tasks_pool):
    n = 0
    for element in tasks_pool:
        if element['due_date'] < datetime.now() and element['done'] is False:
            n += 1
    return n
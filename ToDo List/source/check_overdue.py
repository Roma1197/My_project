from datetime import datetime


def check_overdue(tasks_pool):
    """Shows uncompleted tasks"""
    for element in tasks_pool:
        if element['due_date'] < datetime.now():
            print(element['title'])
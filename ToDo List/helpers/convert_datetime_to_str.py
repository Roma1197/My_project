from datetime import datetime


def convert_datetime_to_str(tasks_pool):
    for element in tasks_pool:
        element['due_date'] = str(element['due_date'])
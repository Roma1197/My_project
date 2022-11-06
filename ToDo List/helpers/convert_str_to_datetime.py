from datetime import datetime


def convert_str_to_datetime(tasks_pool):
    for element in tasks_pool:
        element['due_date'] = datetime.strptime(element['due_date'], '%Y-%m-%d %H:%M:%S')
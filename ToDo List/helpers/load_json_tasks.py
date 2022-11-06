import json
import os
from data.test_data import tasks


def import_json_file(folder, file):
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, folder, file)
    try:
        with open(dir_path, 'r') as my:
            get = my.read()
            tasks = json.loads(get)
            return tasks
    except FileNotFoundError:
        print('Файл з задачами відсутній.')
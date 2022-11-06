import json
from datetime import datetime
import os
from data.test_data import tasks


def save_as_json(folder, file, tasks_pool):
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, folder, file)
    with open(dir_path, 'w') as n:
        json.dump(tasks_pool, n)
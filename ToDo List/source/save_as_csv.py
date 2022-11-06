import csv
import os


def save_as_csv(folder, file, tasks_pool):
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, folder, file)
    with open(dir_path, 'w') as n:
        obj = csv.writer(n)
        obj.writerow(tasks_pool)
from helpers.count_statistics import count_completed, count_uncompleted, count_overdue
from data.test_data import TASK_TEST


def check_stat(tasks_pool):
    tasks = str(len(tasks_pool))
    tasks_done = str(count_completed(tasks_pool))
    tasks_in_process = str(count_uncompleted(tasks_pool))
    overdue_tasks = str(count_overdue(tasks_pool))

    print('Сатистика: ' + '\n'
          + 'Загальна кількість справ - ' + tasks + '\n'
          + 'Кількість виконаних справ - ' + tasks_done + '\n'
          + 'Кількість невиконаних справ - ' + tasks_in_process + '\n'
          + 'Кількість просрочених справ - ' + overdue_tasks)
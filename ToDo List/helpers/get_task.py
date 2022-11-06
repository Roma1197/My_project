from data.test_data import TASK_TEST


def get_task(tasks_pool):
    """Finds a task by its title"""
    my_input = input('Введіть повну назву задачі: ')
    flag = False
    for element in tasks_pool:
        if element['title'].lower() == my_input.lower():
            return element
        else:
            flag = True
    if flag:
        print('Задачу не знайдено.')
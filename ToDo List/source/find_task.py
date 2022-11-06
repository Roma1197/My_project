from data.test_data import TASK_TEST


def find_task(tasks_pool):
    """Finds a task(tasks) by a part of its title and print it(them)"""
    my_input = input('Введіть назву задачі: ')
    found_task = None
    found_task_pool = []
    for element in tasks_pool:
        if my_input in element['title'].lower():
            found_task = element
            found_task_pool.append(found_task)
    if found_task:
        for element in found_task_pool:
            for key in element.keys():
                print(key + ': ' + str(element[key]))
            print('\n')
    else:
        print('Задачу не знайдено.')
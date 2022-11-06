from helpers.get_task import get_task


def del_task(tasks_pool):
    """Deletes the task from task pool"""
    my_obj = get_task(tasks_pool)
    if my_obj:
        tasks_pool.remove(my_obj)
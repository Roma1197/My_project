from helpers.get_task import get_task


def change_done_status(tasks_pool):
    """Function changes the 'done' status of the task, if it was found by name"""
    my_object = get_task(tasks_pool)
    if my_object:
        my_object['done'] = True
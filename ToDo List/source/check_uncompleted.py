def check_uncompleted(tasks_pool):
    """Shows uncompleted tasks"""
    for element in tasks_pool:
        if element['done'] is False:
            print(element['title'])
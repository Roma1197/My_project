def check_completed(tasks_pool):
    """Shows completed tasks"""
    for element in tasks_pool:
        if element['done']:
            print(element['title'])
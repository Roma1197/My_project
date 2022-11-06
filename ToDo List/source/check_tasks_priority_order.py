import operator


def check_priority(tasks_pool):
    """Shows tasks sorted by decreasing priority """
    ordered_list = tasks_pool[:]
    ordered_list.sort(key=operator.itemgetter('priority'))
    for element in ordered_list[::-1]:
        print(element['title'])
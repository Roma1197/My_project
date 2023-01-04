from random import randint

array = []
for i in range(10000):
    array.append(randint(0, 9))

import time


def time_function(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + " took " + str((end - start) * 1000) + " ms")
        return result

    return wrapper


@time_function
def bubble_sort(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    n = len(array)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if array[i - 1] > array[i]:
                swap(i - 1, i)
                swapped = True

    return array


if __name__ == "__main__":
    bubble_sort(array)
    print(array)


begin = 0
end = 4


@time_function
def sort_q(array, begin, end):
    def partition(array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(array, begin, end):
        if begin >= end:
            return
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx - 1)
        quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(array, begin, end):
        if end is None:
            end = len(array) - 1

        return quick_sort_recursion(array, begin, end)

    if __name__ == "__main__":
        quick_sort_recursion(array, begin, end)
        print(array)


sort_q(array, begin, end)

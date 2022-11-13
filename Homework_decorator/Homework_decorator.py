from functools import wraps
import math

def decorator_log(func):
    @wraps(func)
    def wrapper():
        with open('log.txt', 'a', encoding="utf-8") as file_object:
            file_object.write(func.__name__)
        func()
    return wrapper

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print('Before call')
        func()
        print('After call')
    return wrapper

@decorator_log
@my_decorator
def say():
    print("My name is Nick")
say()

@decorator_log
@my_decorator
def number_factorial():
    print(math.factorial(4))
number_factorial()
from datetime import datetime

def exported():
    @wraps(func)
    def wrapper():
        current_datetime = datetime.now()
        print(current_datetime)

    return wrapper

@exported
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def export_to_stdout(self):
        print(f'{self.name} is {self.age} years old')
from datetime import datetime, timedelta


class Animal:

    list_of_animals = list()

    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age
        self.list_of_animals.append(self)

    def time_pointment(self):
        year = int(input('Укажіть рік: '))
        month = int(input('Укажіть місяць: '))
        day = int(input('Укажіть день: '))
        hour = int(input('Укажіть годину: '))
        minutes = int(input('Укажіть минути: '))
        specific_time = datetime(year,month, day, hour, minutes)
        self.appointment = specific_time

    def __str__(self):
        return f'A {self.kind} named {self.name} {self.age} years old'

    def is_vaccinated(self):
        if hasattr(self, 'vaccination_date'):
            return True
        return False

    def get_vaccinated(self):
        if self.kind in ['dog', 'cat']:
            if getattr(self,
                    'vaccination_date',
                    datetime.now() - timedelta(days=730)
                ) < datetime.now() - timedelta(days=365):
                self.vaccination_date = datetime.now()
        else:
            print('We will not vaccinate your animal!')


        name = input('Please, enter your dog\'s name: ')
        age = input('How old is it? ')
        super().__init__(self.__class__.__name__.lower(), name, age)
        self.size = input('What is size of your dog? ')

    def __str__(self):
        return super().__str__() + f' and it is {self.size} sized'

class Cat(Animal):

    def __init__(self):
        name = input('Please, enter your cat\'s name: ')
        age = input('How old is it? ')
        super().__init__(self.__class__.__name__.lower(), name, age)

if __name__ == '__main__':
    my_cat = Cat()
    my_cat.time_pointment()
    print(my_cat.appointment)

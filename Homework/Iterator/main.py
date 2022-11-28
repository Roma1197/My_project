class Iterator:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            temporary_index = self.index
            self.index += 1
            return self.data[temporary_index]
        else:
            raise StopIteration


with open('text.txt', 'r', encoding="utf-8") as file_object:
    my_text = file_object.read()

for element in Iterator(my_text):
    print(element, end='')
print()


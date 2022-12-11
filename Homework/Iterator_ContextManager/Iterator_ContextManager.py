class FileContext:

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file_obj.close()

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

if __name__ == '__main__':
    with FileContext('test_file.txt', 'r') as file:
        for line in file:
            print(line)

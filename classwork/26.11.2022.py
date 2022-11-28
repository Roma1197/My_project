class InclusiveRange:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current_value = 0
        return self

    def __next__(self):
        if self.current_value <= self.limit:
            tmp = self.current_value
            self.current_value += 1
            return tmp
        else:
            raise StopIteration



class Container:

    def __init__(self):
        self.registry = [1,2,3]

    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self.registry):
            tmp_index = self.index
            self.index += 1
            return self.registry[tmp_index]
        else:
            raise StopIteration

    if __name__ == '__main__':
        example_str = 'abcd'
        str_iter = iter(example_str)
        try:
            print(next(str_iter))
            print(next(str_iter))
            print(next(str_iter))
            print(next(str_iter))
            print(next(str_iter))
        except StopIteration:
            print('Iteration is over')
        container = Container()
        for element in container:
            print(element)
        my_range = InclusiveRange(5)




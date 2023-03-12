class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.end:
            raise StopIteration

        self.counter += 1
        return self.counter



for num in custom_range(1, 10):
    print(num)

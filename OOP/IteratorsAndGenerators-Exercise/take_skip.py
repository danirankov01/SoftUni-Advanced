class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.first_number = 0 - step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.counter:
            raise StopIteration

        self.first_number += self.step
        self.counter += 1
        return self.first_number


for number in take_skip(2, 6):
    print(number)

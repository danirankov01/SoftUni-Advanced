class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.index = -1
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.counter += 1

        if self.index == len(self.seq):
            self.index = 0

        if self.number == self.index:
            raise StopIteration

        if self.counter == self.number:
            raise StopIteration

        return self.seq[self.index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

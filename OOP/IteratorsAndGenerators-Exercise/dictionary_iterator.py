class dictionary_iter:
    def __init__(self, d):
        self.d = list(d.items())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.d):
            raise StopIteration

        self.counter += 1
        return self.d[self.counter - 1]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

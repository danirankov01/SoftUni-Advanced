def read_next(*args):
    for first in args:
        for second in first:
            yield second


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

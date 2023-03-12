def fibonacci():
    first = 0
    second = 1
    third = first + second

    yield first
    yield second
    yield third

    while True:
        penultimate = second
        last = third
        current = penultimate + last
        yield current
        second = last
        third = current


generator = fibonacci()
for i in range(15):
    print(next(generator))

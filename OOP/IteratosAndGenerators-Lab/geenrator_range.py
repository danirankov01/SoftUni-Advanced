def genrange(start, end):
    for numbers in range(start, end + 1):
        yield numbers


print(list(genrange(1, 10)))
def squares(n):
    for numbers in range(1, n + 1):
        yield numbers * numbers


print(list(squares(5)))

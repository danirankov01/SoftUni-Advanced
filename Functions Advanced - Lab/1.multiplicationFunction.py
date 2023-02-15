def multiply(*args):
    result = 1
    for i in args:
        result *= i

    return result

result = multiply(1, 2, 3, 4, 5)
print(result)

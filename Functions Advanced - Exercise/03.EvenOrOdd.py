def even_odd(*args):
    command = args[-1]
    numbers = []

    for i in range(len(args) - 1):
        numbers.append(args[i])

    if(command == "even"):
        numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    elif(command == "odd"):
        numbers = list(filter(lambda x: x % 2 != 0, numbers))

    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
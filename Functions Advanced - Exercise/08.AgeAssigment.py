def age_assignment(*args, **kwargs):
    output = {}

    sortedArgs = sorted(args, key=lambda x: (x))
    sortedKwarg = sorted(kwargs.items(), key=lambda x: (x[0]))

    for arg in range(len(sortedArgs)):
        for kwarg in range(arg, len(sortedKwarg)):
            output[sortedArgs[arg]] = sortedKwarg[kwarg][1]
            break

    result = []
    for k in output.keys():
        result.append(f"{k} is {output[k]} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
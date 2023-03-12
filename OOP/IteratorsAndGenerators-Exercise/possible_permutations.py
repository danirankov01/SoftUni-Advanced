def possible_permutations(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            remaining = lst[:i] + lst[i+1:]
            for permutation in possible_permutations(remaining):
                yield [lst[i]] + permutation


[print(n) for n in possible_permutations([1, 2, 3])]

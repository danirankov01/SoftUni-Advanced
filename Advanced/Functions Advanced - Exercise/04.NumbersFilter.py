def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if(k == "even"):
            kwargs[k] = list(filter(lambda x: x % 2 == 0, kwargs[k]))
        elif(k == "odd"):
            kwargs[k] = list(filter(lambda x: x % 2 != 0, kwargs[k]))

    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1])))
    return kwargs



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))



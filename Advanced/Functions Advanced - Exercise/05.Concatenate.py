def concatenate(*args, **kwargs):
    result = ""
    for i in range(len(args)):
        result += args[i]

    for k in kwargs.keys():
        keyword = kwargs[k]
        if(k in result):
            result = result.replace(k, keyword)
    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
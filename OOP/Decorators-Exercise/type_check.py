def type_check(kind):
    def func(function):
        def wrapper(param):
            if type(param) == kind:
                return function(param)

            return "Bad Type"
        return wrapper
    return func


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("result.txt", "a") as result:
            result.write(f"Function {self.function.__name__} was called. Result: {self.function(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)

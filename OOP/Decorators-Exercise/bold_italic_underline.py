def make_bold(function):
    def wrapper(*text):
        return f"<b>{function(*text)}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*text):
        return f"<i>{function(*text)}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*text):
        return f"<u>{function(*text)}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))

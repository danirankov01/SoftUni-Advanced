def tags(tag):
    def decorator(function):
        def wrapper(*text):
            return f"<{tag}>{function(*text)}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

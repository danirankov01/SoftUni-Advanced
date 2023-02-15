def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

person = {
    "name": "Dani",
    "age": 22,
    "town": "Sofia"
}

print(get_info(**person))
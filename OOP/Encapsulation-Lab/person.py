class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


p = Person("Dani", 22)
print(p.get_name())
print(p.get_age())
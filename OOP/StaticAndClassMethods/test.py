class Validator:
    @staticmethod
    def check_if_name_is_empty_or_null(name, error='Name is not valid'):
        if not name.strip():
            raise ValueError(error)

    @staticmethod
    def check_if_age_is_in_range(value, min_age, max_age, error):
        if value < min_age or value > max_age:
            raise ValueError(error)


class Person:
    MIN_AGE = 0
    MAX_AGE = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_name_is_empty_or_null(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.check_if_age_is_in_range(
            value,
            self.MIN_AGE,
            self.MAX_AGE,
            f'Age should be between {self.MIN_AGE} and {self.MAX_AGE}')
        self.__age = value


class Employee(Person):
    MIN_AGE = 18
    MAX_AGE = 65

    def __init__(self, name, age):
        super().__init__(name, age)


p = Person('Pesho', 7)
e = Employee('Gosho', 19)
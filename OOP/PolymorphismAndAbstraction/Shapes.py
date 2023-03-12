import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return self.__radius * math.pi * 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


c = Circle(5)
print(c.calculate_perimeter())
print(c.calculate_area())

from abc import ABC

from project.animals.animal import Bird
from project.food import Food, Meat, Seed, Vegetable, Fruit


class Owl(Bird, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        eatable = [Meat]
        if food.__class__ not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        eatable = [Meat, Seed, Vegetable, Fruit]
        if food.__class__ not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

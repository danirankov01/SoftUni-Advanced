from abc import ABC

from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        eatable = [Vegetable, Fruit]
        if food not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        eatable = [Meat]
        if food not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        eatable = [Vegetable, Meat]
        if food not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        eatable = [Meat]
        if food not in eatable:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity\

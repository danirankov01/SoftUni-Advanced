from project_Need_For_Speed.product import Product


class Drink(Product):
    def __init__(self, name):
        self.name = name
        self.quantity = 10
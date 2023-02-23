from project_Need_For_Speed.product import Product


class Food(Product):
    def __init__(self, name):
        self.name = name
        self.quantity = 15
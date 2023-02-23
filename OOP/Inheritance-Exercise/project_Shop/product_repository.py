from project_Need_For_Speed.product import Product


class ProductRepository(Product):
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: Product):
        for pr in self.products:
            if pr.__class__.__name__ == product_name.__class__.__name__:
                return pr

    def remove(self, product_name):
        for count, pr in enumerate(self.products):
            if pr.name == product_name:
                del self.products[count]

    def __repr__(self):
        result = ""

        for pr in self.products:
            result += f"{pr.name}: {pr.quantity}\n"

        return result.rstrip()
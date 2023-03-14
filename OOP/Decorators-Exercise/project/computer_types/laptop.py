from project.computer_types.computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        valid_processors = {
            "AMD Ryzen 9 5950X": 900,
            "inter Core-i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

        minimum_ram = 2
        price = 100
        rams = {}
        while True:
            if minimum_ram > 64:
                break

            rams[minimum_ram] = price
            minimum_ram += minimum_ram
            price += price

        if processor not in valid_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in rams:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        laptop = Laptop(self.manufacturer, self.model)
        laptop.processor = processor
        laptop.ram = ram
        laptop.price = rams[ram]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {laptop.price}$."

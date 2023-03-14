from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        valid_processors = {
            "AMD Ryzen 7 5700G": 500,
            "Inter Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

        minimum_ram = 2
        price = 100
        rams = {}
        while True:
            if minimum_ram > 128:
                break

            rams[minimum_ram] = price
            minimum_ram += minimum_ram
            price += price

        if processor not in valid_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in rams:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        comp = Computer(self.manufacturer, self.model)
        comp.processor = processor
        comp.ram = ram
        comp.price = rams[ram]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {comp.price}$."


from project.computer_types.computer import Computer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        valid_types = ["Desktop Computer", "Laptop"]
        if type_computer not in valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Desktop Computer":
            comp = Computer(manufacturer, model)
            conf = comp.configure_computer(processor, ram)
            self.warehouse.append(conf)
            return conf

        if type_computer == "Laptop":
            laptop = Laptop(manufacturer, model)
            conf = laptop.configure_computer(processor, ram)
            self.warehouse.append(conf)
            return conf

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for comp in self.warehouse:
            if comp <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)

                return f"{comp} sold for {client_budget}$."

        return "Sorry, we don't have a computer for you."

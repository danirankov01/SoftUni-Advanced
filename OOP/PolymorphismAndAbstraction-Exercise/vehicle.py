from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, fuel):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, fuel):
        needed_fuel = (self.fuel_consumption + self.CONSUMPTION) * fuel
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, fuel):
        needed_fuel = (self.fuel_consumption + self.CONSUMPTION) * fuel
        if self.fuel_quantity >= needed_fuel:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

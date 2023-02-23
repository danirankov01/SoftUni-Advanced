from project_Need_For_Speed.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def drive(self, kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption

from project_Need_For_Speed.car import Car


class FamilyCar(Car):
    def drive(self, kilometers):
        if self.fuel >= kilometers * self.fuel_consumption:
            self.fuel -= kilometers * self.fuel_consumption

from project_Need_For_Speed.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers):
        if self.fuel >= kilometers * self.DEFAULT_FUEL_CONSUMPTION:
            self.fuel -= kilometers * self.DEFAULT_FUEL_CONSUMPTION

from project_Need_For_Speed.vehicle import Vehicle


class Motorcycle(Vehicle):
    def drive(self, kilometers):
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= kilometers * self.fuel_consumption

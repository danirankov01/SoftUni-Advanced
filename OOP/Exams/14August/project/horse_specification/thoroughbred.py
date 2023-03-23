from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED_OF_HORSE = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        self.speed = min(self.MAX_SPEED_OF_HORSE, self.speed + 3)

class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print("Max Speed = " + str(self.__max_speed))


car = Car()
car.drive()
Car.__max_speed = _Car__max_speed = 20
car.drive()

from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(35, 60)

    def test_fuel_consumption(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_initializing(self):
        self.assertEqual(self.vehicle.fuel, 35)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 60)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_driving_with_less_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_correct_driving(self):
        self.vehicle.drive(1)
        self.assertEqual(self.vehicle.fuel, 33.75)

    def test_refueling_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_refueling(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)

    def test_output(self):
        result = str(self.vehicle)
        expected = "The vehicle has 60 horse power with 35 " \
                   "fuel left and 1.25 fuel consumption"

        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()

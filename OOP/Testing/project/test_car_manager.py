from unittest import TestCase, main
from car_manager import Car


class TestsCar(TestCase):
    def setUp(self):
        self.car = Car("Lancia", "Ypsilon", 5, 35)

    def test_initializing(self):
        self.assertEqual(self.car.make, "Lancia")
        self.assertEqual(self.car.model, "Ypsilon")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 35)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_empty_make_of_the_car(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_empty_model_of_the_car(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refueling_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refueling(self):
        self.car.refuel(self.car.fuel_capacity + 10)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_driving_car_with_less_fuel_than_we_need(self):
        self.car.fuel_amount = 10

        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_driving(self):
        self.car.fuel_amount = 10
        self.car.drive(5)
        self.assertEqual(self.car.fuel_amount, 9.75)


if __name__ == "__main__":
    main()

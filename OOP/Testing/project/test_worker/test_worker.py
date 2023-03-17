from unittest import TestCase, main
from project.test_worker.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Dani", 1000, 100)

    def test_when_initializing(self):
        self.assertEqual("Dani", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_when_receives_salary(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_energy_when_worker_is_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_if_worker_energy_is_less_than_or_zero(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increase_energy_after_rest(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_information_about_the_worker(self):
        worker_info = self.worker.get_info()
        self.assertEqual("Dani has saved 0 money.", worker_info)


if __name__ == "__main__":
    main()

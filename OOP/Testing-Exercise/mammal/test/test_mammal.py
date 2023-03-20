from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Rufas", "dog", "bau-bau")

    def test_initializing(self):
        self.assertEqual(self.mammal.name, "Rufas")
        self.assertEqual(self.mammal.type, "dog")
        self.assertEqual(self.mammal.sound, "bau-bau")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_mammal_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Rufas makes bau-bau")

    def test_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), "Rufas is of type dog")


if __name__ == "__main__":
    main()
    
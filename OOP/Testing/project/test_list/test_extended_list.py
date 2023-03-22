from unittest import TestCase, main

from extended_list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.list_numbers = IntegerList(1, 2, 3)

    def test_getting_the_list(self):
        self.assertEqual(self.list_numbers, self.)


if __name__ == "__main__":
    main()

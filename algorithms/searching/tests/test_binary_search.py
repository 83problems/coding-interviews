import random
import unittest

from algorithms.searching.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_value_exists(self):
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        value_to_find = random.choice(values)
        expected = values.index(value_to_find)
        self.assertEqual(binary_search(values, value_to_find), expected)

    def test_value_not_exists(self):
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        value_to_find = 15
        expected = -1
        self.assertEqual(binary_search(values, value_to_find), expected)

    def test_empty_list(self):
        values = []
        value_to_find = 0
        expected = -1
        self.assertEqual(binary_search(values, value_to_find), expected)


if __name__ == 'main':
    unittest.main()

import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_big_val(self):
        res = area(100)
        self.assertEqual(res, 10000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
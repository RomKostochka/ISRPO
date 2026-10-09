import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(6, 7)
        self.assertEqual(res, 21)

    def test_area_big_val(self):
        res = area(100, 200)
        self.assertEqual(res, 10000)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_normal(self):
        res = perimeter(6, 7, 8)
        self.assertEqual(res, 21)
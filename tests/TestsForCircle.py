import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_big_val(self):
        res = area(100)
        self.assertAlmostEqual(res, math.pi * 10000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)
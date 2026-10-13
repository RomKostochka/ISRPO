import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_big_val(self):
        res = area(10**9,10**9)
        self.assertEqual(res,10**18)

    def test_basic_perimeter(self):
        res = perimeter(10,20)
        self.assertEqual(res,60)
        
    def test_new_perimeter(self):
            res = perimeter(10,20)
            self.assertEqual(res,80)
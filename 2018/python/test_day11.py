import unittest
from day11 import *

class TestSum(unittest.TestCase):
  def test_get_power(self):
    self.assertEqual(get_power_level(3,5,8),4)
    self.assertEqual(get_power_level(122,79,57),-5)  
    self.assertEqual(get_power_level(101,153,71),4)  
    self.assertEqual(get_power_level(217,196,39),0)

  def test_get_largest_power(self):
    self.assertEqual(get_largest_power(18), (33,45))
    self.assertEqual(get_largest_power(42), (21,61))
    # self.assertEqual(get_largest_power(6878), (20,34))

  # def test_get_summed_area(self):
    # self.assertEqual(get_summed_area_table([[31,2,4,33,5,36],[12,26,9,10,29,25],[13,17,21,22,20,18]]),[[31,33,37,70,75,111],[43,71,84,127,161,222],[56,101,135,200,254,333]])

  def test_get_size(self):
    # self.assertEqual(get_largest_power_square(18),(90,269,16))
    # self.assertEqual(get_largest_power_square(42),(232,251,12))
    self.assertEqual(get_largest_power_square(6878),(232,251,12))
if __name__ == '__main__':
    unittest.main()
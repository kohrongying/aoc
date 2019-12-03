import unittest
from day6 import *

class TestSum(unittest.TestCase):
  def test_get_coordinates(self):
    self.assertEqual(get_coordinates("1, 1 "), (1,1))
  
  def test_manhanttan_distance(self):
    self.assertEqual(manhattan_distance(1,1,5,1), 4)
    self.assertEqual(manhattan_distance(8,3,5,1), 5)

  def test_get_closest_coor(self):
    self.assertEqual(get_closest_coor(0,0,[(1,1),(1,6),(8,3)]), 0)

  # def test_get_bounded(self):
  #   coors = parse_file('day6.txt')
  #   self.assertEqual(get_bounded_coors(coors), (1, 1, 8, 9))

  # def test_find_bounded(self):
  #   coors = parse_file('day6.txt')
  #   self.assertEqual(find_bounded_points(coors), [3,4])
  
  # def test_parse_grid(self):
  #   self.assertEqual(parse_grid(), 17)

  # def test_manhanttan_sum(self):
  #   coors = parse_file('day6_test.txt')
  #   self.assertEqual(get_manhantan_sum(4, 3, coors), 30)

  def test_get_region(self):
    self.assertEqual(get_region(), 30)

if __name__ == '__main__':
    unittest.main()
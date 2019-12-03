import unittest
from day10 import *

class TestSum(unittest.TestCase):

  def test_parse_line(self):
    f = open('day10-test.txt', 'r')

    self.assertEqual(parse_line("position=< 9,  1> velocity=< 0,  2>"), ([9,1],[0,2]))
    self.assertEqual(parse_line("position=<-6, 10> velocity=< 2, -2>"), ([-6,10],[2,-2]))
    self.assertEqual(parse_line("position=< 9,  1> velocity=< 0,  2>"),([9,1],[0,2]))
    

  def test_update_position(self):
    self.assertEqual(update_position(3,9,1,-2,3), [6,3])
if __name__ == '__main__':
  unittest.main()
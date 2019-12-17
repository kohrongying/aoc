from unittest import TestCase, main
from day16 import generate_multiplier, solve

class TestDays(TestCase):
  def test_generate_multiplier(self):
    pattern = [0,1,0,-1]
    self.assertEqual(generate_multiplier(1, pattern, 8), [1,0,-1,0,1,0,-1,0])
    self.assertEqual(generate_multiplier(2, pattern, 9), [0,1,1,0,0,-1,-1,0,0])
  
  def test_solve(self):
    self.assertEqual(solve('80871224585914546619083218645595', 100), [2,4,1,7,6,1,7,6])
    self.assertEqual(solve('19617804207202209144916044189917', 100), [7,3,7,4,5,4,1,8])
    self.assertEqual(solve('69317163492948606335995924319873', 100), [5,2,4,3,2,1,3,3])
  
if __name__ == '__main__':
  main()
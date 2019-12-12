from unittest import TestCase, main
from day10 import calc_gradient, calc_direction, calc_magnitude, calc_angle

class TestDay10(TestCase):
  def test_calc_gradent(self):
    self.assertEqual(calc_gradient((3,4), (1,0)), 2)
    self.assertEqual(calc_gradient((2,2), (1,0)), 2)
  
  def test_calc_direction(self):
    self.assertEqual(calc_direction((2,2), (2,3)), 'U')
    self.assertEqual(calc_direction((2,2), (2,1)), 'D')
    self.assertEqual(calc_direction((2,2), (3,2)), 'R')
    self.assertEqual(calc_direction((2,2), (1,2)), 'L')
    self.assertEqual(calc_direction((2,2), (4,1)), 'R')

  def test_calc_magnitude(self):
    self.assertEqual(calc_magnitude((1,1), (4,5)), 5)
  
  def test_calc_angle(self):
    self.assertEqual(calc_angle((0,0), (3,3)), 135)
    self.assertEqual(calc_angle((0,0), (3,3**0.5)), 120)

if __name__ == '__main__':
  main()
from unittest import TestCase, main
from day4 import is_increasing, has_adjacent, custom_rle

class TestJoke(TestCase):
  def test_increasing(self):
    self.assertEqual(is_increasing(123), True)
    self.assertEqual(is_increasing(1223), True)
    self.assertEqual(is_increasing(123123), False)

  def test_adjacent(self):
    self.assertEqual(has_adjacent(123), False)
    self.assertEqual(has_adjacent(1223), True)
    self.assertEqual(has_adjacent(121123), True)

  def test_rle(self):
    self.assertEqual(custom_rle(112233), [2, 2, 2])
    self.assertEqual(custom_rle(113334), [2, 3, 1])


if __name__ == '__main__':
  main()
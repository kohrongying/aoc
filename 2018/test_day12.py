import unittest
from day12 import *

class TestSum(unittest.TestCase):
  def test_parse_line(self):
    self.assertEqual(parse_line("####. => #"), "####.")
  
  def test_get_pattern(self):
    initial_state = "#.#.#....##...##...##...#.##.#.###...#.##...#....#.#...#.##.........#.#...#..##.#.....#..#.###"
    self.assertEqual(get_pattern(0, initial_state), "..#.#")
    self.assertEqual(get_pattern(1, initial_state), ".#.#.")
    self.assertEqual(get_pattern(2,initial_state),"#.#.#")
    self.assertEqual(get_pattern(93,initial_state),"###..")
    self.assertEqual(get_pattern(92,initial_state),".###.")


if __name__ == '__main__':
    unittest.main()
from unittest import TestCase, main
from day3 import summ, left, right, up, down, get_intersections, solve, get_manhattan_distance

class TestJoke(TestCase):
  def test_sum(self):
    self.assertTrue(summ(1,1), 2)

  def test_get_intersections(self):
    path1 = "R8,U5,L5,D3"
    path2 = "U7,R6,D4,L4"
    intersects = [(3,3), (6,5)]
    self.assertCountEqual(get_intersections(path1, path2), intersects)
  
  def test_manhat(self):
    origin=(0,0)
    self.assertEqual(get_manhattan_distance(origin, (3,3)), 6)

  def test_solve(self):
    path1 = "R8,U5,L5,D3"
    path2 = "U7,R6,D4,L4"
    self.assertEqual(solve(path1, path2), 6)

    path1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    path2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    self.assertEqual(solve(path1, path2), 135)


if __name__ == '__main__':
  main()
import unittest
from day7 import *

class TestSum(unittest.TestCase):
  def test_parse_line(self):
    self.assertEqual(parse_line("Step C must be finished before step A can begin."), ("C","A"))

  def test_parse_file(self):
    self.assertEqual(parse_file('day7-test.txt'),[("C","A"),("C",'F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')])

  def test_get_all_elements(self):
    # self.assertEqual(get_all_elements([("C","A"),("C",'F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]), ['A', 'C', 'B', 'E', 'D', 'F'])
    self.assertEqual(get_all_elements(parse_file('day7.txt')), [])

  def test_get_dep_elements(self):
    arr = [("C","A"),("C",'F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
    self.assertEqual(get_dependent_elements(arr), ['A', 'B', 'E', 'D', 'F'])    

  def test_get_indep_elements(self):
    arr = parse_file('day7.txt')
    all = get_all_elements(arr)
    dep = get_dependent_elements(arr)
    self.assertEqual(get_independent_elements(all, dep), ['C'])
  
  def test_find_indep_steps(self):
    arr = [("C","A"),("C",'F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
    self.assertEqual(find_indep_steps(arr, 'C'), [("C","A"),("C",'F')])

  def test_sort_steps(self):
    self.assertEqual(sort_steps([("C","F"),("C",'A')]), [("C","A"),("C",'F')])

  def test_remove_indep(self):
    arr = [("C","A"),("C",'F'),('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
    arr2 = [('A','B'),('A','D'),('B','E'),('D','E'),('F','E')]
    self.assertEqual(remove_indep_steps(arr, 'C'), arr2)

  def test_get_last_element(self):
    self.assertEqual(get_last_element(['A', 'C', 'B', 'E', 'D', 'F'],"CABDF"), 'E')
  
  # def test_get_order(self):
  #   self.assertEqual(get_order('day7.txt'), "CABDFE")

if __name__ == '__main__':
    unittest.main()
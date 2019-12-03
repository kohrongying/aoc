import unittest
from day8 import *

class TestSum(unittest.TestCase):
  def test_get_value(self):
    node = {'value': 0, 'num_entries': 1, 'children': [{'value': 99, 'num_entries': 1, 'children': [], 'num_child': 0, 'entries': []}], 'num_child': 0, 'entries': [2]}
    self.assertEqual(get_value(node), 0)
    node2 = {'value': 0, 'num_entries': 3, 'children': [{'value': 33, 'num_entries': 3, 'children': [], 'num_child': 0, 'entries': []}, {'value': 0, 'num_entries': 1, 'children': [{'value': 99, 'num_entries': 1, 'children': [], 'num_child': 0, 'entries': []}], 'num_child': 0, 'entries': [2]}], 'num_child': 0, 'entries': [1, 1, 2]}
    self.assertEqual(get_value(node2), 66)

    node3 = build_tree(open('day8.txt','r').readline())
    self.assertEqual(get_value(node3), 23054)
        

if __name__ == '__main__':
    unittest.main()
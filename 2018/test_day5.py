import unittest
from day5 import *

class TestSum(unittest.TestCase):
    def test_remove_letter_from_polymer(self):
      self.assertEqual(remove_letter_from_polymer("dabAcCaCBAcCcaDA",["c","C"]), "dabAaCBAcCcaDA")

if __name__ == '__main__':
    unittest.main()
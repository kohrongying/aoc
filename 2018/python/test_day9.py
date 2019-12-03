import unittest
from day9 import *

class TestSum(unittest.TestCase):
  def test_add_marble(self):
    self.assertEqual(add_marble([],0,0),([0], 0))
    self.assertEqual(add_marble([0],0,1), ([0,1],1))
    self.assertEqual(add_marble([0,1], 1, 2), ([0,2,1],1))
    self.assertEqual(add_marble([0,2,1], 1,3), ([0,2,1,3],3))
    self.assertEqual(add_marble([0,2,1,3],3,4),([0,4,2,1,3],1))  
    
  def test_remove_marble(self):
    arr = [0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    end = [0, 16, 8, 17, 4, 18, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15]
    end2 = [0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 3, 14, 7, 15]
    # self.assertEqual(remove_marble(arr,13), ((end, 6), 9))
    self.assertEqual(remove_marble(arr,2), ((end2, 18), 13))


  def test_get_new_player(self):
    self.assertEqual(get_new_player(9,8),0)
    self.assertEqual(get_new_player(9,0),1)
    self.assertEqual(get_new_player(9,3),4)   

  def test_get_score(self):
    # self.assertEqual(get_highest_score(build_game(9, 25)), 32) 
    # self.assertEqual(get_highest_score(build_game(10, 1618)), 8317) 
    # self.assertEqual(get_highest_score(build_game(13, 7999)), 146373) 
    # self.assertEqual(get_highest_score(build_game(17, 1104)), 2764) 
    # self.assertEqual(get_highest_score(build_game(21, 6111)), 54718)
    # self.assertEqual(get_highest_score(build_game(30,5807)), 37305)
    self.assertEqual(get_highest_score(build_game(429,7090100)), 399645)

if __name__ == '__main__':
    unittest.main()
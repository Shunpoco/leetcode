import unittest
from remove_dupolicates import Solution

class TestRemoveDuplicates(unittest.TestCase):
  def setUp(self):
    self.testCases = [
      {
        'nums': [1,2,2],
        'want': 2,
      },
      {
        'nums': [-1,-1,0,0,2,2,2,3,4,4,4,4,5,],
        'want': 6,
      },
    ]

  def test_want(self):
    s = Solution()
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        self.assertEqual(s.removeDuplicates(testCase['nums']), testCase['want'])

if __name__ == '__main__':
  unittest.main()

import unittest

from two_sum import twoSum

class TestTwoSum(unittest.TestCase):
  def setUp(self):
    self.testCases = [
      {
        'nums': [2, 7, 11, 15],
        'target': 9,
        'want': [0, 1],
      },
      {
        'nums': [3, 2, 4],
        'target': 6,
        'want': [1, 2],
      },
      {
        'nums': [3, 3],
        'target': 6,
        'want': [0, 1],
      },
      {
        'nums': [-1, 10, 9, 7],
        'target': 6,
        'want': [0, 3],
      },
      {
        'nums': [0, 0, 10, 12],
        'target': 0,
        'want': [0, 1],
      },
      {
        'nums': [2, 5, 5, 11],
        'target': 10,
        'want': [1, 2],
      },
    ]

  def test_want(self):
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        self.assertEqual(twoSum(testCase['nums'], testCase['target']), testCase['want'])

if __name__ == '__main__':
  unittest.main()
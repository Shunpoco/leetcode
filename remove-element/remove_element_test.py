import unittest

from remove_element import Solution

class TestRemoveElement(unittest.TestCase):
  def setUp(self):
    self.testCases = [
      {
        'nums': [3, 2, 2, 3],
        'val': 3,
        'expected': 2,
      },
      {
        'nums': [0, 1, 2, 2, 3, 0, 4, 2],
        'val': 2,
        'expected': 5,
      },
      {
        'nums': [0, 0, 0, 0],
        'val': 0,
        'expected': 0,
      },
      {
        'nums': [0, 0, 0, 0],
        'val': 0,
        'expected': 0,
      },
      {
        'nums': [],
        'val': 100,
        'expected': 0,
      },
    ]

  def test(self):
    s = Solution()
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        self.assertEqual(
          s.removeElement(
            testCase['nums'],
            testCase['val']
          ),
          testCase['expected']
        )

if __name__ == '__main__':
  unittest.main()

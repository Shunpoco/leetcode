import unittest

from reverse_integer import Solution

class TestReverse(unittest.TestCase):
  def setUp(self):
    self.testCases =  [
      {
        'x': 123,
        'want': 321,
      },
      {
        'x': -123,
        'want': -321,
      },
      {
        'x': 120,
        'want': 21,
      },
      {
        'x': 0,
        'want': 0,
      },
      {
        'x': -1234000100,
        'want': -10004321,
      },
      {
        'x': 99999999999999999,
        'want': 0,
      },
    ]

  def testRev(self):
    sol = Solution()
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        res = sol.reverse(testCase['x'])
        self.assertEqual(res, testCase['want'])

if __name__ == '__main__':
  unittest.main()
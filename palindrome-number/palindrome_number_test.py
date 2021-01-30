import unittest

from palindrome_number import Solution

class TestIsPalindrome(unittest.TestCase):
  def setUp(self):
    self.testCases = [
      {
        'x': 121,
        'want': True,
      },
      {
        'x': -121,
        'want': False,
      },
      {
        'x': 10,
        'want': False,
      },
      {
        'x': 0,
        'want': True,
      },
      {
        'x': 123321,
        'want': True
      },
    ]

  def test_want(self):
    s = Solution()
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        self.assertEqual(s.isPalindrome(testCase['x']), testCase['want'])

if __name__ == '__main__':
  unittest.main()

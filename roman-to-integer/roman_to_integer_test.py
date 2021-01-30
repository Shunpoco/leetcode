import unittest
from roman_to_integer import Solution

class TestRomanToInt(unittest.TestCase):
  def setUp(self):
    self.testCases = [
      {
        's': 'III',
        'want': 3,
      },
      {
        's': 'IV',
        'want': 4,
      },
      {
        's': 'IX',
        'want': 9,
      },
      {
        's': 'LVIII',
        'want': 58,
      },
      {
        's': 'MCMXCIV',
        'want': 1994,
      },
    ]

  def test_want(self):
    s = Solution()
    for testCase in self.testCases:
      with self.subTest(testCase=testCase):
        self.assertEqual(s.romanToInt(testCase['s']), testCase['want'])

if __name__ == '__main__':
  unittest.main()
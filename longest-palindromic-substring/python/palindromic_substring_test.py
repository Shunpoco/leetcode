import unittest

from palindromic_substring import Solution


class TestPalindromic(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.testCases = [
            {
                's': 'babad',
                'want': 'bab',
            },
            {
                's': 'cbbd',
                'want': 'bb',
            },
            {
                's': 'a',
                'want': 'a',
            },
            {
                's': 'ac',
                'want': 'a',
            },
        ]


    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.longestPalindrome(tc['s']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

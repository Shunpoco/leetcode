import unittest
from word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.testCases = [
            {
                's': 'leetcode',
                'wordDict': ['leet', 'code'],
                'want': True,
            },
            {
                's': 'applepenapple',
                'wordDict': ['apple', 'pen'],
                'want': True,
            },
            {
                's': 'catsandog',
                'wordDict': ['cats', 'dog', 'sand', 'and', 'cat'],
                'want': False,
            },
            {
                's': 'cars',
                'wordDict': ['car', 'ca', 'rs'],
                'want': True,
            },
        ]

    
    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.wordBreak(tc['s'], tc['wordDict']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

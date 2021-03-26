import unittest

from valid import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                's': 'anagram',
                't': 'nagaram',
                'want': True,
            },
            {
                's': 'rat',
                't': 'car',
                'want': False,
            },
            {
                's': '東京都',
                't': '京都東',
                'want': True,
            },
            {
                's': 'ab',
                't': 'b',
                'want': False,
            },
        ]

    def test(self):
        s = Solution()
        for tc in self.testCases:
            with self.subTest(testCase=tc):
                self.assertEqual(
                    s.isAnagram(tc['s'], tc['t']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

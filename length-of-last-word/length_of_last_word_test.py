import unittest
from length_of_last_word import Solution


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                's': 'Hello World',
                'expected': 5,
            },
            {
                's': ' ',
                'expected': 0,
            },
            {
                's': 'a ',
                'expected': 1,
            },
            {
                's': 'b     ',
                'expected': 1,
            },
        ]

    def test(self):
        s = Solution()
        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.lengthOfLastWord(testCase['s']),
                    testCase['expected'],
                )

if __name__ == '__main__':
    unittest.main()
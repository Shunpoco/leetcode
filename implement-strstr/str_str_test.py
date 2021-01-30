import unittest

from str_str import Solution

class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'haystack': 'hello',
                'needle': 'll',
                'expected': 2,
            },
            {
                'haystack': 'aaaaa',
                'needle': 'bba',
                'expected': -1,
            },
            {
                'haystack': '',
                'needle': '',
                'expected': 0,
            },
            {
                'haystack': 'lollee',
                'needle': 'll',
                'expected': 2,
            },
        ]

    def test(self):
        s = Solution()
        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.strStr(
                        testCase['haystack'],
                        testCase['needle'],
                    ),
                    testCase['expected'],
                )

if __name__ == '__main__':
    unittest.main()

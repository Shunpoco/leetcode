import unittest

from strstr import Solution

class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'haystack': 'hello',
                'needle': 'll',
                'want': 2,
            },
            {
                'haystack': 'aaaaa',
                'needle': 'bba',
                'want': -1,
            },
            {
                'haystack': '',
                'needle': '',
                'want': 0,
            },
            {
                'haystack': 'aa',
                'needle': 'aaa',
                'want': -1,
            },
            {
                'haystack': 'a',
                'needle': 'a',
                'want': 0,
            },
            {
                'haystack': 'mississippi',
                'needle': 'issip',
                'want': 4,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.strStr(tc['haystack'], tc['needle']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

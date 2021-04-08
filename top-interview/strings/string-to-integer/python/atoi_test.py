import unittest

from atoi import Solution

class TestAtoi(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            # {
            #     's': '42',
            #     'want': 42,
            # },
            # {
            #     's': '   -42',
            #     'want': -42,
            # },
            # {
            #     's': '4193 with words',
            #     'want' :4193,
            # },
            # {
            #     's': 'words and 987',
            #     'want': 0,
            # },
            # {
            #     's': '-91283472332',
            #     'want': -2147483648,
            # },
            {
                's': '  0000000000012345678',
                'want': 12345678,
            },
        ]

        self.s = Solution()

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.myAtoi(tc['s']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

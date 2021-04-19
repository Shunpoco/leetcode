import unittest

from find_digits import Solution

class TestFindNumbers(unittest.TestCase):
    def setUp(self):
        self.soluton = Solution()
        self.testCases = [
            {
                'nums': [555, 901, 482, 1771],
                'want': 1,
            },
            {
                'nums': [12,345,2,6,7896],
                'want': 2,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.soluton.findNumbers(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

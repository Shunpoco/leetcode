import unittest

from square import Solution

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'nums': [-4, -1, 0, 3, 10],
                'want': [0, 1, 9, 16, 100],
            },
            {
                'nums': [-7, -3, 2, 3, 11],
                'want': [4, 9, 9, 49, 121],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.sortedSquares(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

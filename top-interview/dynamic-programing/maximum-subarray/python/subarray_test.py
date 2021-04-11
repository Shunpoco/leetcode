import unittest

from subarray import Solution


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'nums': [-2, 1, -3, 4, -1, 2, 1, -5, 4],
                'want': 6
            },
            {
                'nums': [1],
                'want': 1,
            },
            {
                'nums': [5, 4, -1, 7, 8],
                'want': 23,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.maxSubArray(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

import unittest

from best_time import Solution

class TestBestTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'prices': [7,1,5,3,6,4],
                'want': 5,
            },
            {
                'prices': [7,6,4,3,1],
                'want': 0,
            },
            {
                'prices': [2,4,1],
                'want': 2,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.maxProfit(tc['prices']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

import unittest

from best_time import Solution

class TestBestTime(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'prices': [7,1,5,3,6,4],
                'want': 7,
            },
            {
                'prices': [1,2,3,4,5],
                'want': 4,
            },
            {
                'prices': [7,6,4,3,1],
                'want': 0,
            },
        ]

    def test(self):
        s = Solution()
        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.maxProfit(testCase['prices']),
                    testCase['want']
                )

if __name__ == '__main__':
    unittest.main()

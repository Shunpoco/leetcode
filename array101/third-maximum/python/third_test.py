import unittest

from third import Solution

class TestThirdMaximum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.testCases = [
            {
                'nums': [3,2,1],
                'want': 1,
            },
            {
                'nums': [1,2],
                'want': 2,
            },
            {
                'nums': [2,2,3,1],
                'want': 1,
            },
            {
                'nums': [5,2,2],
                'want': 5,
            },
            {
                'nums': [2,2,2,1],
                'want': 2,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.thirdMax(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

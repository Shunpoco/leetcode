import unittest

from single_number import Solution

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'nums': [2,2,1],
                'want': 1,
            },
            {
                'nums': [4,1,2,1,2],
                'want': 4,
            },
            {
                'nums': [1],
                'want': 1,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(testCase=tc):
                self.assertEqual(
                    self.solution.singleNumber(tc['nums']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

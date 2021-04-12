import unittest

from code import Solution

class TestBeautifulArrangement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'n': 3,
                'k': 1,
                'want': [1,2,3],
            },
            {
                'n': 3,
                'k': 2,
                'want': [2,1,3],
            },
            {
                'n': 5,
                'k': 3,
                'want': [2,3,1,4,5],
            },
            {
                'n': 5,
                'k': 4,
                'want': [3,2,4,1,5],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.constructArray(tc['n'], tc['k']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

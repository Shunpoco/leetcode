import unittest

from max_consecutive import Solution

class TestMaxConsecutive(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums': [1,0,1,1,0,1],
                'want': 2,
            },
            {
                'nums': [1,1,0,1,1,1],
                'want': 3,
            },
        ]
        self.solution = Solution()

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.findMaxConsecutiveOnes(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

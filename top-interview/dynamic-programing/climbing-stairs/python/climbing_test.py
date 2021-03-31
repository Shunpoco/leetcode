import unittest

from climbing import Solution

class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'n': 2,
                'want': 2,
            },
            {
                'n': 3,
                'want': 3,
            },
            {
                'n': 4,
                'want': 5,
            },
            {
                'n': 45,
                'want': 1836311903,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.climbStairs(tc['n']),
                    tc['want'],
                )

    def tearDown(self):
        print('Well done!')


if __name__ == '__main__':
    unittest.main()
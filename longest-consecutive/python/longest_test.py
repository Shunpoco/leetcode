import unittest
from longest import Solution


class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'nums': [100, 4, 200, 1, 3, 2],
                'want': 4,
            },
            {
                'nums': [0,3,7,2,5,8,4,6,0,1],
                'want': 9,
            },
            {
                'nums': [],
                'want': 0,
            },
            {
                'nums': [1,2,0,1],
                'want': 3,
            },
            {
                'nums': [9,1,-3,2,4,8,3,-1,6,-2,-4,7],
                'want': 4,
            }
        ]


    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.longestConsecutive(tc['nums']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

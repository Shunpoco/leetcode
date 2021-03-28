import unittest

from rotate import Solution

from typing import List

class TestSolution(Solution):
    def __init__(self, nums: List[int], k: int):
        self.nums = nums
        self.k = k

    def testRotate(self):
        self.rotate(self.nums, self.k)

class TestRotate(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums': [1,2,3,4,5,6,7],
                'k': 3,
                'want': [5,6,7,1,2,3,4],
            },
            {
                'nums': [-1, -100, 3, 99],
                'k': 2,
                'want': [3,99,-1,-100],
            },
            {
                'nums': [1,2,3,4,5],
                'k': 0,
                'want': [1,2,3,4,5],
            },
            {
                'nums': [0],
                'k': 2,
                'want': [0],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(testCase=tc):
                s = TestSolution(nums=tc['nums'], k=tc['k'])
                s.testRotate()
                self.assertEqual(
                    s.nums,
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

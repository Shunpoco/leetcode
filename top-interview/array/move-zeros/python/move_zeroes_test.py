import unittest
from typing import List
from move_zeroes import Solution

class TestSolution(Solution):
    def __init__(self, nums: List[int]):
        self.nums = nums

    def move(self) -> None:
        self.moveZeroes(self.nums)


class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums': [0,1,0,3,12],
                'want': [1,3,12,0,0],
            },
            {
                'nums': [0],
                'want': [0],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                s = TestSolution(tc['nums'])
                s.move()
                self.assertEqual(
                    s.nums,
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

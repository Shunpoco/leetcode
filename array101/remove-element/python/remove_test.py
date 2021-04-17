import unittest
from typing import List
from dataclasses import dataclass
from remove import Solution

@dataclass
class TestSolution(Solution):
    nums: List[int]

    def testRemoveElement(self, val:int)->int:
        return self.removeElement(self.nums, val)

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums': [3,2,2,3],
                'val': 3,
                'want': [2,2],
            },
            {
                'nums': [0,1,2,2,3,0,4,2],
                'val': 2,
                'want': [0,1,3,0,4],
            },
            {
                'nums': [],
                'val': 3,
                'want': [],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                s = TestSolution(tc['nums'])
                v = s.testRemoveElement(tc['val'])
                self.assertEqual(
                    s.nums[:v],
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

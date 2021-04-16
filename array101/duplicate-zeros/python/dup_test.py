import unittest
from typing import List

from dup import Solution

class TestSolution(Solution):
    def __init__(self, arr: List[int]):
        self.arr = arr

    def testDuplicateZeros(self):
        self.duplicateZeros(self.arr)



class TestDup(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'arr': [1,0,2,3,0,4,5,0],
                'want': [1,0,0,2,3,0,0,4],
            },
            {
                'arr': [1,2,3],
                'want': [1,2,3],
            },
            {
                'arr': [1,0,2,3,0,4,5,0, 6, 7,8],
                'want': [1,0,0,2,3,0,0,4,5,0,0],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                s = TestSolution(tc['arr'])
                s.testDuplicateZeros()
                self.assertEqual(
                    s.arr,
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

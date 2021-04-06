from typing import List

import unittest

from rotate_image import Solution

class TestSolution(Solution):
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def testRotate(self):
        self.rotate(self.matrix)


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'matrix': [[1,2,3],[4,5,6],[7,8,9]],
                'want': [[7,4,1],[8,5,2],[9,6,3]],
            },
            {
                'matrix': [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
                'want': [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
            },
            {
                'matrix': [[1]],
                'want': [[1]],
            },
            {
                'matrix': [[1,2], [3,4]],
                'want': [[3,1], [4,2]],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                s = TestSolution(tc['matrix'])
                s.testRotate()
                self.assertEqual(
                    s.matrix,
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

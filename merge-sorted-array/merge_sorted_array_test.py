import unittest

from merge_sorted_array import Solution

from typing import List

class TestSolution(Solution):
    def __init__(self, nums1: List[int], m: int, nums2: List[int], n: int):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n

    def testMerge(self):
        self.merge(self.nums1, self.m, self.nums2, self.n)


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums1': [1,2,3,0,0,0],
                'm': 3,
                'nums2': [2,5,6],
                'n': 3,
                'expected': [1,2,2,3,5,6],
            },
            {
                'nums1': [4, 5, 6, 0, 0, 0],
                'm': 3,
                'nums2': [1,2,3],
                'n': 3,
                'expected': [1,2,3,4,5,6],
            },


        ]

    def test(self):
        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                s = TestSolution(
                    testCase['nums1'],
                    testCase['m'],
                    testCase['nums2'],
                    testCase['n'],
                )
                s.testMerge()
                self.assertEqual(s.nums1, testCase['expected'])

if __name__ == '__main__':
    unittest.main()

                                    
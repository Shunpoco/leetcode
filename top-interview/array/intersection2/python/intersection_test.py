import unittest

from intersection import Solution

class TestIntersect(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.testCases = [
            {
                'nums1': [1,2,2,1],
                'nums2': [2,2],
                'want': [2,2],
            },
            {
                'nums1': [4,9,5],
                'nums2': [9,4,9,8,4],
                'want': [4,9],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.intersect(tc['nums1'], tc['nums2']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

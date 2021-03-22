import unittest

from validate import Solution
from validate import TreeNode

class TestValidate(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'root': TreeNode(2, TreeNode(1), TreeNode(3)),
                'want': True,
            },
            {
                'root': TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),
                'want': False,
            },
            {
                'root': TreeNode(2),
                'want': True,
            },
            {
                'root': TreeNode(1, TreeNode(1)),
                'want': False,
            },
            {
                'root': TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))),
                'want': True,
            }

        ]

    def test(self):
        s = Solution()
        for testCase in self.testCases:
            print(testCase)
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.isValidBST(testCase['root']),
                    testCase['want'],
                )

if __name__ == '__main__':
    unittest.main()

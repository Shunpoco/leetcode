import unittest

from path_sum import TreeNode, Solution

class TestPathSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'root': TreeNode(
                    5, TreeNode(4,TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
                ),
                'targetSum': 22,
                'want': True,
            },
            {
                'root': TreeNode(
                    1, TreeNode(2), TreeNode(3),
                ),
                'targetSum': 5,
                'want': False,
            },
            {
                'root': TreeNode(
                    1, TreeNode(2), None,
                ),
                'targetSum': 0,
                'want': False,
            },
            {
                'root': TreeNode(
                    1, TreeNode(2), None,
                ),
                'targetSum': 1,
                'want': False,
            },
            {
                'root': None,
                'targetSum': 0,
                'want': False,
            },
        ]


    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.hasPathSum(tc['root'], tc['targetSum']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()

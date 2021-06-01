class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        result = self._sum(root, 0)

        if result > pow(2, 31)-1:
            result = 0

        return result


    def _sum(self, node: TreeNode, val: int) -> int:
        if node is None:
            return 0

        val *= 10
        val += node.val

        if node.left is None and node.right is None:
            return val

        leftSum = self._sum(node.left, val)
        rightSum = self._sum(node.right, val)

        return leftSum + rightSum

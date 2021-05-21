class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if self._isLeaf(root):
            if targetSum-root.val == 0:
                return True
            return False

        nextTS = targetSum - root.val

        leftR = self.hasPathSum(root.left, nextTS)
        rightR = self.hasPathSum(root.right, nextTS)

        return leftR | rightR


    def _isLeaf(self, node: TreeNode) -> bool:
        if node is None:
            return False

        if node.left is not None or node.right is not None:
            return False

        return True

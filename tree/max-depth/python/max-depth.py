class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self._count(root, 0)

    def _count(self, root: TreeNode, count: int) -> int:
        if root is None:
            return count

        count += 1

        return max(self._count(root.left, count), self._count(root.right, count))


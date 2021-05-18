from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        self._preorder(root)

        return self.result

    def _preorder(self, root: TreeNode):
        if root is None:
            return

        self.result.append(root.val)

        self._preorder(root.left)
        self._preorder(root.right)

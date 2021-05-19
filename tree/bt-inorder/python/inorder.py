from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        self._inorder(root)

        return self.result

    def _inorder(self, node: TreeNode):
        if node is None:
            return

        self._inorder(node.left)

        self.result.append(node.val)

        self._inorder(node.right)

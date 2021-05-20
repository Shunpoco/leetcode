from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        self._postorder(root)

        return self.result

    def _postorder(self, node: TreeNode) -> None:
        if node is None:
            return

        self._postorder(node.left)
        self._postorder(node.right)

        self.result.append(node.val)

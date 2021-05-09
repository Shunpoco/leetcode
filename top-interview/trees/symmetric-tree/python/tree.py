from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    zero = -101
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True

        return self._list(root.left, [], 'left') == self._list(root.right, [], 'right')

    def _list(self, node: TreeNode, l: List[int], pri: str) -> List[int]:
        if node is None:
            l.append(self.zero)
            return l

        l.append(node.val)

        if pri == 'left':
            l = self._list(node.left, l, 'left')
            l = self._list(node.right, l, 'left')

        else:
            l = self._list(node.right, l, 'right')
            l = self._list(node.left, l, 'right')

        return l

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        r = self._toList(root.right, 'r', [])
        l = self._toList(root.left, 'l', [])

        print(r)
        print(l)

        if l == r:
            return True

        return False

    def _toList(self, node: TreeNode, rotate: str, l: List[int]) -> List[int]:
        if node is None:
            l.append(-101)
            return l

        l.append(node.val)

        if rotate == 'r':
            l = self._toList(node.right, 'r', l)
            l = self._toList(node.left, 'l', l)

        if rotate == 'l':
            l = self._toList(node.left, 'l', l)
            l = self._toList(node.right, 'r', l)

        return l

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        return self._paths(root, targetSum, [])

    def _paths(self, root: TreeNode, targetSum: int, l: List[List[int]]) -> List[List[int]]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            if targetSum-root.val == 0:
                return l.append(root.val)
            return []

        newTS = targetSum - root.val
        l.append(root.val)
        lSum = self._paths(root.left, newTS, l)
        rSum = self._paths(root.right, newTS, l)


        return lSum.extend(rSum)

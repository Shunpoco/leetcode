from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        return self._pathSum(root, targetSum, [])


    def _pathSum(self, node: TreeNode, target: int, res: List):
        if node is None:
            return []

        target -= node.val
        res.append(node.val)

        if self._isLeaf(node):
            if target == 0:
                return [res]
            return []

        results = []
        lefts = self._pathSum(node.left, target, res.copy())
        rights = self._pathSum(node.right, target, res.copy())
        if len(lefts) > 0:
            results.extend(lefts)
        if len(rights) > 0:
            results.extend(rights)

        return results
    

    def _isLeaf(self, node: TreeNode) -> bool:
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True

        return False

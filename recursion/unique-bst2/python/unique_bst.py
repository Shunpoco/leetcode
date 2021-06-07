from typing import List, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self._generate(n, 1)
    
    def _generate(self, n: int, num: int) -> List[TreeNode]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(val=num)]

        result = []

        for r in range(n):
            l = (n-1) - r
            lefts = self._generate(l, num)
            rootVal = num + l
            rights = self._generate(r, num+l+1)

            for left in lefts:
                for right in rights:
                    root = TreeNode(val=rootVal)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result

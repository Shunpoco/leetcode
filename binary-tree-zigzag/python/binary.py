from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        candidates = [root]

        return self._zigzag(candidates, result, True)

    def _zigzag(self, candidates: List[TreeNode], result: List[List[int]], isClockWise: bool):
        s = list(set(candidates))
        if s[0] is None and len(s) == 1:
            return result
        next = []
        res = []
        l = len(candidates)
        for i in range(l):
            node = candidates[i]
            if node is not None:
                if isClockWise:
                    res.append(node.val)
                else:
                    res.insert(0, node.val)
                next.append(node.left)
                next.append(node.right)

        result.append(res)

        return self._zigzag(next, result, not(isClockWise))

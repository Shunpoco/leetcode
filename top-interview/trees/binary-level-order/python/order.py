from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        result.append([root.val])

        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        lenL = len(left)
        lenR = len(right)
        maxLen = max(lenL, lenR)

        for i in range(maxLen):
            t = []
            if lenL > i:
                t.extend(left[i])
            if lenR > i:
                t.extend(right[i])

            result.append(t)

        return result
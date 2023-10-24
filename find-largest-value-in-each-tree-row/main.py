from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = [(root, 0)]
        result = []

        while q:
            v, level = q.pop(0)
            if len(result) == level:
                result.append(v.val)
            elif v.val > result[level]:
                result[level] = v.val

            if v.left:
                q.append((v.left, level+1))
            if v.right:
                q.append((v.right, level+1))

        return result


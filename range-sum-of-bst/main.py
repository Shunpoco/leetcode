# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = [root]
        r = 0

        while len(q) > 0:
            v = q.pop(0)
            if low <= v.val and v.val <= high:
                r += v.val
            
            if v.val > low and v.left is not None:
                q.append(v.left)

            if v.val < high and v.right is not None:
                q.append(v.right)

        return r

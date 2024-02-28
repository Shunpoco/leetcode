# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = -1
        r = 0
        q = [(root, 0)]

        while len(q) > 0:
            node, depth = q.pop(0)

            if d < depth:
                d = depth
                r = node.val

            if node.left is not None:
                q.append((node.left, depth+1))
            if node.right is not None:
                q.append((node.right, depth+1))

        return r


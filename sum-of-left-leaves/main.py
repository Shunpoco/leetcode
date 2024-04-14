# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0

        queue = [(root, False)]

        while queue:
            node, isLeft = queue.pop(0)

            if node.left is None and node.right is None and isLeft:
                result += node.val

            if node.left is not None:
                queue.append((node.left, True))

            if node.right is not None:
                queue.append((node.right, False))

        return result


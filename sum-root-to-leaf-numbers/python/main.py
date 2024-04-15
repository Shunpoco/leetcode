# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.r = 0

        def exec(node: Optional[TreeNode], v: int):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.r += v * 10 + node.val
                return
            v *= 10
            v += node.val

            exec(node.left, v)
            exec(node.right, v)

        exec(root, 0)

        return self.r


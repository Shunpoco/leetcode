# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = [root1]
        v1 = []

        while len(stack) > 0:
            node = stack.pop(-1)
            if node.left is None and node.right is None:
                v1.append(node.val)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        stack.append(root2)
        v2 = []
        while len(stack):
            node = stack.pop(-1)
            if node.left is None and node.right is None:
                v2.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return v1 == v2

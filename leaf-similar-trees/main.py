# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        self.leafs(root1, r1)
        self.leafs(root2, r2)

        return r1 == r2

    def leafs(self, node, result):
        if node.left is None and node.right is None:
            result.append(node.val)

        if node.left is not None:
            self.leafs(node.left, result)

        if node.right is not None:
            self.leafs(node.right, result)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.calc(root, 0)

        return root


    def calc(self, node, fp) -> int:
        t = node.val

        if node.right is not None:
            t += self.calc(node.right, fp)

        node.val = t + fp

        if node.left is not None:
            t += self.calc(node.left, fp + t)

        return t




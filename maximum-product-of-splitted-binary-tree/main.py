from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        self.nodeSum(root, sums)
        rval = sums.pop(-1)
        result = 0

        for s in sums:
            v = ((rval-s) * s)
            result = max([result, v])

        return result % 1000000007


    def nodeSum(self, node: Optional[TreeNode], arr: List[int]) -> int:
        if node is None:
            return 0

        r = node.val
        r += self.nodeSum(node.left, arr)
        r += self.nodeSum(node.right, arr)

        arr.append(r)
        return r

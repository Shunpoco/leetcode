# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, 0)]
        sums = []

        while len(stack) > 0:
            v, l = stack.pop(-1)
            if len(sums) - 1 < l:
                sums.append(0)

            sums[l] += v.val

            if v.left is not None:
                stack.append((v.left, l+1))

            if v.right is not None:
                stack.append((v.right, l+1))

        if len(sums) < k:
            return -1

        sums.sort()
        
        return sums[len(sums)-k]
        

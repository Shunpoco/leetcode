from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        m = int(len(nums) / 2)
        root = TreeNode(nums[m], None, None)

        left = nums[:m]
        right = nums[m+1:]

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root
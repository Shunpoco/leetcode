# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0

        stack = [(root, 0)]

        while len(stack) > 0:
            node, val = stack.pop()
            if node is None:
                continue

            val = val ^ (1 << node.val)

            if node.left is None and node.right is None:
                if val & (val-1) == 0:
                    count += 1

            else:
                stack.append((node.left, val))
                stack.append((node.right, val))

        return count

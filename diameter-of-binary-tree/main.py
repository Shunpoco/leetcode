# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calc(node):
            if node is None:
                return -1, -1
            
            left = calc(node.left)
            right = calc(node.right)

            d = left[0] + right[0] + 2

            return max(left[0], right[0])+1, max(left[1], right[1], d)

        _, result = calc(root)

        return result


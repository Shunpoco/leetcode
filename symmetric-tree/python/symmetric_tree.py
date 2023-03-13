from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        
        return self.exec(root.left, root.right)

    def exec(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None and right is not None or left is not None and right is None:
            return False

        if left.val != right.val:
            return False

        return self.exec(left.left, right.right) & self.exec(left.right, right.left)

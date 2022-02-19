from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)] # (TreeNode, whether it is left or right)
        
        result = 0
        
        while len(stack) > 0:
            node, isLeft = stack.pop()
            
            if node.left is None and node.right is None and isLeft:
                result += node.val
            else:
                if node.left:
                    stack.append((node.left, True))
                if node.right:
                    stack.append((node.right, False))
                    
        return result

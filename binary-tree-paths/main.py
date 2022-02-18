from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(f"{root.val}", root)]
        
        result = []
        
        while len(stack) > 0:
            s, c = stack.pop()
            if c.left is None and c.right is None:
                result.append(s)
            else:
                if c.left:
                    stack.append((f"{s}->{c.left.val}", c.left))
                if c.right:
                    stack.append((f"{s}->{c.right.val}", c.right))
                    
        return result


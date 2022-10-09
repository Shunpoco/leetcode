from typing import List, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        r = []
        stack = [root]
        
        while len(stack) > 0:
            v = stack.pop()
            
            r.append((k-v.val, v))
            
            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
        
        for v in r:
            if self.search(root, v):
                return True
            
        return False
    
    def search(self, root: Optional[TreeNode], v: Tuple[int, TreeNode]) -> bool:
        if root is None:
            return False
        
        if root.val == v[0]:
            if root != v[1]:
                return True
            return False
        
        if root.val > v[0]:
            return self.search(root.left, v)
        if root.val < v[0]:
            return self.search(root.right, v)

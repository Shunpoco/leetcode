"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        stack =  [(root, 1)]
        
        count = 1
        
        while len(stack) > 0:
            n, l = stack.pop()
            if count < l:
                count = l
            
            for c in n.children:
                if c:
                    stack.append((c, l+1))
                
        return count

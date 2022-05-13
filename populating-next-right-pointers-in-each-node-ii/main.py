"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [(root, 1)]
        
        while len(queue) > 0:
            (node, level) = queue.pop(0)
            
            if len(queue) > 0 and queue[0][1] == level:
                node.next = queue[0][0]
              
            if node:
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
                
        return root

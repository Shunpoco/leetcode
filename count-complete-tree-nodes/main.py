# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = [(root, 1)]
        count = 0
        while len(queue):
            node, level = queue.pop(0)
            count += 1
            
            if node.left:
                queue.append((node.left, level+1))
            else:
                break
            if node.right:
                queue.append((node.right, level+1))
            else:
                break
                
        count += len(queue)
        
        return count

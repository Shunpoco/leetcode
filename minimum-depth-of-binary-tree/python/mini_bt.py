# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 0
        
        return self._depth(root, count)
        
    def _depth(self, node: TreeNode, count: int) -> int:
        if node is None:
            return pow(10, 5) + 1
        
        count += 1
        
        
        if node.left is None and node.right is None:
            return count
        
        
        count = min(
            self._depth(node.left, count),
            self._depth(node.right, count),
        )
        
        return count

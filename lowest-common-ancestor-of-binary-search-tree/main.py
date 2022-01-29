# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        if root.val > p.val and root.val < q.val or root.val < p.val and root.val > q.val:
            return root
        
        if root.val > p.val:
            n = root.left
        else:
            n = root.right
        
        return self.lowestCommonAncestor(n, p, q)

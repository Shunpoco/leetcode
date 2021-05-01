class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if root.val == val:
            return root

        l = self.searchBST(root.left, val)

        if l is not None:
            return l

        r = self.searchBST(root.right, val)
        if r is not None:
            return r

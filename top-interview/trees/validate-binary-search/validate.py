class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    MIN = -2 ** 31 -1
    MAX = 2 ** 31
    def isValidBST(self, root: TreeNode) -> bool:
        return self._valid(root, self.MAX, self.MIN)


    def _valid(self, root: TreeNode, maxVal: int, minVal: int) -> bool:
        if root is None:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        return self._valid(root.left, root.val, minVal) and\
            self._valid(root.right, maxVal, root.val)
        


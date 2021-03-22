class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._valid(root)[0]

    def _valid(self, root: TreeNode) -> (bool, int, int):
        '''
        return (isBST, max, min)
        '''
        result = (True, root.val, root.val)

        if root.left is None and root.right is None:
            return result

        left, right = None, None
        if root.left is not None:
            left = self._valid(root.left)
            
        if root.right is not None:
            right = self._valid(root.right)


        if left is not None:
            if left[0] == False or left[1] >= root.val:
                return (False, 0, 0)
            result = (True, result[1], left[2])
        
        if right is not None:
            if right[0] == False or right[2] <= root.val:
                return (False, 0, 0)
            result = (True, right[1], result[2])

        return result
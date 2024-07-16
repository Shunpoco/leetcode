# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        sPass = self.route(root, startValue)
        dPass = self.route(root, destValue)        

        i, j = 0, 0

        while i < len(sPass) and j < len(dPass) and sPass[i] == dPass[j]:
            i += 1
            j += 1

        r = "U" * (len(sPass)-i)
        r += dPass[j:]

        return r


    def route(self, root, val) -> str:
        if root.val == val:
            return ""

        if root.left is None and root.right is None:
            return "-1"

        r = "-1"
        if root.left:
            t = self.route(root.left, val)
            if t != "-1":
                r = "L" + t

        if root.right:
            t = self.route(root.right, val)
            if t != "-1":
                r = "R" + t

        return r

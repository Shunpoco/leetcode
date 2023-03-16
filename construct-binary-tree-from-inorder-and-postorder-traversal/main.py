from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        rootv = postorder.pop(-1)
        idx = 0
        for i, v in enumerate(inorder):
            if v == rootv:
                idx = i
                break            

        root = TreeNode(rootv)

        if len(inorder) > 1:

            # left
            if idx != 0:
                i = inorder[:idx]
                root.left = self.buildTree(i, postorder[:len(i)])
            # right
            if idx == 0:
                root.right = self.buildTree(inorder[idx+1:], postorder)
            else:
                l = len(inorder[:idx])
                root.right = self.buildTree(inorder[idx+1:], postorder[l:])

        return root


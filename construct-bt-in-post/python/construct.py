from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None

        rootVal = postorder[len(postorder)-1]
        root = TreeNode(rootVal)

        inRootIdx = inorder.index(rootVal)

        inLeft = inorder[:inRootIdx]
        inRight = inorder[inRootIdx+1:]

        postLeft = postorder[:len(inLeft)]
        postRight = postorder[len(inLeft):len(postorder)-1]

        root.left = self.buildTree(inLeft, postLeft)
        root.right = self.buildTree(inRight, postRight)

        return root

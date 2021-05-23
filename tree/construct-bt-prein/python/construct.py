from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal)

        inRootIdx = inorder.index(rootVal)

        inLeft = inorder[:inRootIdx]
        inRight = inorder[inRootIdx+1:]

        preLeft = preorder[1:len(inLeft)+1]
        preRight = preorder[len(inLeft)+1:]

        root.left = self.buildTree(preLeft, inLeft)
        root.right = self.buildTree(preRight, inRight)

        return root
